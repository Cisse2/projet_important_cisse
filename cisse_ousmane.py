# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:40:54 2020

@author: PC
"""

voyelles=["a","e","i","u","o","y"]
numbers = list("1234567890")
vCounter = 0
cCounter = 0
nbrCounter = 0
nounCounter = 0

file = open("fichier.txt","r")
fileContent = str(file.read())
nbrLines = len(file.readlines())
file.seek(0)
for i in fileContent:
    if i in voyelles:
        vCounter = vCounter + 1
        continue
    elif i in numbers:
        nbrCounter = nbrCounter +1
        continue
    elif i != ' ' and i not in voyelles and i not in numbers:
        cCounter = cCounter + 1
        continue
    elif i == ' ':
        nounCounter = nounCounter + 1
        continue

newFile = open("compteRendu.txt","w")
newFile.write(f"nombre de ligne :{len(file.readlines())}\n")
newFile.write(f"Le nombre de mot du premier fichier est de {nounCounter}\n")
newFile.write(f"Il y a {vCounter} voyelles ")
newFile.write(f"Et {cCounter} Consonnes dans le premier fichier.\n")
if nbrCounter != 0:
    newFile.write("Le premier fichier contient des chiffre")
elif nbrCounter == 0:
    newFile.write("Il y a pas de chiffre dans le premier fichier")
file.close()
newFile.close()

openingNewFile = open("compteRendu.txt","r")
print(openingNewFile.read())
openingNewFile.close()
