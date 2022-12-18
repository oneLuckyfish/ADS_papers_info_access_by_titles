import ads
import pandas as pd
import re

token = 'J7Ycch7jXIt8GmxHK2vYxs48DrpFRrBVcRuFGjzt'  # ads上获取的token，每个用户每天搜索次数有限制
data = pd.read_csv('lamostpapers_test.csv')
titles = data.loc[:, 'title']
# print(titles)
# titles = ["TYC 1337-1137-1 and TYC 3836-0854-1: Two Low-mass Ratio, Deep Overcontact Systems Near the End Evolutionary Stage of Contact Binaries"]
DOI = []
Bibcode = []
ArXiv = []
no = 1

for query in titles:
    print(no, " " + query)
    query = 'title:\"' + query + '\"'
    try:
        retrieve = ads.SearchQuery(q=query, token=token)
        retrieve.execute()
        no += 1
        if retrieve.response.numFound == 0:
            DOI.append("None")
            Bibcode.append("None")
            ArXiv.append("None")
            print("Doi: None")
            print("Bibcode: None")
            print("ArXiv: None")
            continue

        Do = retrieve.articles[0].doi
        if Do is not None:
            DOI.append(Do[0])
            print("Doi: " + Do[0])
        else:
            DOI.append("None")
            print("Doi: None")

        Bib = retrieve.articles[0].bibcode
        if Bib is not None:
            Bibcode.append(Bib)
            print("Bibcode: " + Bib)
        else:
            Bibcode.append("None")
            print("Bibcode: None")

        Ident = retrieve.articles[0].identifier
        i = 0
        for it in Ident:
            if it[0:5] == "arXiv":
                ArXiv.append(it)
                print("ArXiv: " + it)
                i += 1
                break
        if i == 0:
            ArXiv.append("None")
            print("ArXiv: None")
    except Exception as e:
        query = query.replace('-', " ")
        no += 1
        retrieve = ads.SearchQuery(q=query, token=token)
        retrieve.execute()
        if retrieve.response.numFound == 0:
            DOI.append("None")
            Bibcode.append("None")
            ArXiv.append("None")
            print("Doi: None")
            print("Bibcode: None")
            print("ArXiv: None")
            continue

        Do = retrieve.articles[0].doi
        if Do is not None:
            DOI.append(Do[0])
            print("Doi: " + Do[0])
        else:
            DOI.append("None")
            print("Doi: None")

        Bib = retrieve.articles[0].bibcode
        if Bib is not None:
            Bibcode.append(Bib)
            print("Bibcode: " + Bib)
        else:
            Bibcode.append("None")
            print("Bibcode: None")

        Ident = retrieve.articles[0].identifier
        i = 0
        for it in Ident:
            if it[0:5] == "arXiv":
                ArXiv.append(it)
                print("ArXiv: " + it)
                i += 1
                break
        if i == 0:
            ArXiv.append("None")
            print("ArXiv: None")

# print(DOI)
# print(Bibcode)
# print(ArXiv)

data = pd.DataFrame(data)
data['Doi'] = DOI
data['Bibcode'] = Bibcode
data['ArXiv'] = ArXiv

data.to_csv("./final_csv.csv", index=False, sep=",")
