'''
Verifica di pari o dispari con specifica di segno
Chiedi un numero intero e determina se è positivo o negativo,
e se è pari o dispari. Il programma deve distinguere tra
"Positivo Pari", "Positivo Dispari", "Negativo Pari" e "Negativo Dispari".
'''

# commento per riga

n=int(input("inserisci un numero: "))

if n>0:
    print("il numero è positivo")
else:
    print("il numero è negativo")
if n%2==0:
    print("e pari")
else:
    print("e dispari")