print("Hello world") #wersja3.x
# printf "Hello World" # wersja2.x

#def main():
#    for elem in kolekcja:
#        if costam < 0:


imie = "Ala"
imie = 0
imie = None

# łańcuchy znaków

imie = "Ala"
print(type(imie))

imie = str("Ala")
# imie = str(100) # "100"
# imie[0] = "0" nie jest mutowalny

imie = imie.lower()
print (imie)

# Typy liczbowe

liczba = 1
liczbaf = 4.5
liczba = liczba * 2

print(liczba)
print(type(liczba))
print(type(liczbaf))

print(0.1+0.2 == 0.3)
print((1/10)+(2/10)==(3/10))

print(f"{0.1:.32f}")
print(f"{0.2:.32f}")
# Decimal lub zaokrąglanie

liczba = ("100")
print(int(liczba))
print(int(liczba, 2))
bin(100)

print("Ala " + "ma kota")

print("Ala" + " ma " + str(5) + " kotów")
print("Ala ma  {} kotów".format(5))
print("Ala ma  {1}{0} kotów".format(5,4))
# f-string python 3.7
ilosc_kotow = 5
print(f"Ala ma  {ilosc_kotow}")