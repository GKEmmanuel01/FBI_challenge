import requests
from bs4 import Beautifulsoup

response = requests.get("http://127.0.0.1:5501//index.html")
soup = Beautifulsoup(response.text, "html.parser")
images = soup.find_all("img")
for img in images:
    print(img["src"])
titres_h1 = soup.find_all("h1")
titres_h2 = soup.find_all("h2")
titres_h3 = soup.find_all("h3")
print ("LES TITRES")

for h1 in titres_h1:
    print(h1.text)

for h2 in titres_h2:
    print(h2.text)

for h3 in titres_h3:
    print(h3.text)

paragraphes = soup.find_all("p")
for p in paragraphes:
    print (p.text)
formulaire = soup.find_all ("form")

for f in formulaire:
    print(f.text)

liens = soup.find_all("a")
for a in liens:
    print(a.text)
