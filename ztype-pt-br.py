import pandas
import random

dicionario = {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": [], "I": [], "J": [], "K": [], "L": [], "M": [], "N": [], "O": [], "P": [], "Q": [], "R": [], "S": [], "T": [], "U": [], "V": [], "W": [], "X": [], "Y": [], "Z": []}
c = 0
alfabeto = list(dicionario.keys())
string = ""
level = {}

df = pandas.read_csv("br-sem-acentos.txt")
for i in df["a"]:
    if (i[0]).lower() == alfabeto[c].lower():
        dicionario[alfabeto[c]].append(i)
    else:
        c += 1

num_of_levels = int(input("Escolha a quantidade de levels: \n"))

for x in range(0, num_of_levels): 
    for i in alfabeto:
        if len(dicionario[i]) > 0:
            string += (dicionario[i][(random.randint(0, (len(dicionario[i])-1)))]) + " "
            level[x] = string

finalstr = ""

for i in level:
    finalstr += (level[i] + "\n")

print(finalstr)