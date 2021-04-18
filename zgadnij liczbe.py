import random
random.seed()


niezgadl = True
liczba = random.randint(1,100)
while niezgadl:
    print("zgadnij moja liczbe (1-100)")
    zmienna = int(input())
    if zmienna == liczba:
        print("brawo! zgadles")
        niezgadl = False
    if zmienna < liczba:
        print("jest wieksza, sprobuj ponownie")
    if zmienna > liczba:
        print(" jest mniejsza, sprobuj ponownie")