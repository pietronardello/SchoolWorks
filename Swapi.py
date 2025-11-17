#Pietro Nardello
'''Utilizzando il servizio API fornito da "Swapi" (https://swapi.dev/), 
    attraverso uno script in python leggere il file JSON ritornato dall'API e, 
    utilizzando dei dizionari, stampare in un file json:
- Per ogni personaggio il nome, l'altezza e il colore dei capelli;
- Per ogni pianeta il nome, il periodo di rotazione e il periodo orbitale
- Per ogni navicella il nome, il modello e il costo in crediti


Successivamente per ogni categoria creare una classe e convertire il JSON in una lista di ogetti di quella classe.
(Esempio: avrò una lista 'personaggi' dove ogni elemento della lista è un oggetto di tipo personaggio 
e conterrà gli elementi richiesti sopra)

EXTRA:

Sul file precedentemente utilizzato scrivere poi per ogni film:
- I 3 veicoli più costosi
- La lista di personaggi presenti in quel film divisi per specie
- Tutti i pianeti con clima arido'''

import requests
URL = "https://swapi.dev/api/"

#people/
r = requests.get(URL + "people/")
dati = r.json()
personaggi = []

while dati["next"] != None:
    for x in dati["results"]:
        diz = {}
        diz["nome"]      = x["name"]
        diz["altezza"]   = x["height"]
        diz["capelli"]   = x["hair_color"]

        personaggi.append(diz)

    r = requests.get(dati["next"])
    dati = r.json()


#pianeta

r = requests.get(URL + "/planets")
info = r.json()

pianeti = []

while(info['next'] != None):
    for x in info['results']:
        pers = {}
        
        pers['nome']        =   x['name']
        pers['rotazione']   =   x['rotation_period']
        pers['orbitale']    =   x['orbital_period']

        pianeti.append(pers)

    r = requests.get(info["next"])
    info = r.json()


#navicella

r = requests.get(URL + "starships/")
nano = r.json()

navicelle = []

while(nano['next'] != None):
    for x in nano['results']:
        navi = {}

        navi["nome"]    =   x["name"]
        navi["modello"] =   x["model"]
        navi["costo"]   =   x["cost_in_credits"]

        navicelle.append(navi)
    r = requests.get(nano["next"])
    nano = r.json()    


#output

print(personaggi)
print(pianeti)
print(navicelle)


