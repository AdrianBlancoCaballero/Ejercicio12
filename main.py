# Ejercicio 12

PALABRAS = "palabras.txt"
FRASES = "frases.txt"

archivo = open(PALABRAS, "r")
palabras = {}
frases = []

class FindPal:
    def __init__(self, PALABRAS, FRASES, archivo, palabras, frases):
        self.PALABRAS = PALABRAS
        self.FRASES = FRASES
        self.archivo = archivo
        self.palabras = palabras
        self.frases = frases


for linea in archivo:
    palabras[linea.strip()] = []

archivo = open(FRASES, "r")

for f in archivo:
    frases.append(f.strip())

    for p in palabras:
        palabras[p].append(f.lower().count(p))

archivo.close()

print("Lista palabras: \n", palabras)
print("Frases: \n", frases)
print("Palabras en frases: \n", palabras)