# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
# przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi

def generator(kod_1,kod_2):
    dwie_cyfry_1 = int(kod_1.split('-')[0])
    trzy_cyfry_1 = int(kod_1.split('-')[1])
    dwie_cyfry_2 = int(kod_2.split('-')[0])
    trzy_cyfry_2 = int(kod_2.split('-')[1])

    while dwie_cyfry_1 <= dwie_cyfry_2:
        if dwie_cyfry_1 == dwie_cyfry_2:
            while trzy_cyfry_1 <= trzy_cyfry_2:
                print('{}-{:03d}'.format(dwie_cyfry_1,trzy_cyfry_1))
                trzy_cyfry_1 += 1

        else:
            while trzy_cyfry_1 < 1000:
                print('{}-{:03d}'.format(dwie_cyfry_1,trzy_cyfry_1))
                trzy_cyfry_1 += 1
        dwie_cyfry_1 += 1
        trzy_cyfry_1 = 0




# ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
# 1-n = [1,2,3,4,5,...,10]
# np. n=10
# wejście: [2,3,7,4,9], 10
# wyjście: [1,5,6,8,10]

def brakuje(lis,n):
    lista = []
    
    for element in range(1, n + 1):
        if element not in lis:
            lista.append(element)
    return lista


# ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.

def liczby():
    liczba = 2.0
    while liczba <= 5.5:
        print(liczba)
        liczba += 0.5



