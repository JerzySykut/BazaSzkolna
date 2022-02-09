import sys

typy = ["uczen", "nauczyciel","wychowawca","koniec"]
szkoła = []


class Uczen:
    def __init__(self):
        self.imie_nazwisko = ""
        self.sala = ""


    def pobierz (self):
        self.imie_nazwisko = input ()
        self.sala = input()



class Nauczyciel:
    def __init__(self):
        self.imie_nazwisko = ""
        self.przedmiot = []
        self.sale = []

    def pobierz (self):
        self.imie_nazwisko = input()
        self.przedmiot = input()
        while True:
            _sala = input()
            if not _sala:
                break
            self.sale.append(_sala)

class Wychowawca:
    def __init__(self):
        self.nazwa = ""
        self.sale = []

    def pobierz(self):
        self.nazwa = input()
        while True:
            sala = input()
            if not sala:
                break
            self.sale.append(sala)


class Sala:
    def __init__(self):
        self.numer = ""

    def numersali(self):
        self.numer = True






while True:
    typ = input()
    if typ not in typy:
        print("Bledny argument")
        exit()
    elif typ == "uczen":
        osoba = Uczen()
    elif typ == "nauczyciel":
        osoba = Nauczyciel()
    elif typ == "wychowawca":
        osoba = Wychowawca()
    elif typ == "koniec":
        break

    osoba.pobierz()
    szkoła.append(osoba)

    continue
#szukamy klasy
znalezione = []
szukana = sys.argv[1]
for x in szkoła:
    if type(x) is Wychowawca:
        if szukana in x.sale:
            znalezione.append(x)
    elif type(x) is Uczen:
        if x.sala == szukana:
            znalezione.append(x)
if znalezione.__len__() > 0:
    for z in znalezione:
        if type(z) is Uczen:
            print(z.imie_nazwisko)
        else:
            print(z.nazwa)
    exit()

wychowawca = None
for x in szkoła:
    if type(x) is Wychowawca:
        if szukana == x.nazwa:
            wychowawca = x
            break
if wychowawca is not None:
    for x in szkoła:
        if type(x) is Uczen and x.sala in wychowawca.sale:
            print(x.imie_nazwisko)
    exit()

nauczyciel = None
for x in szkoła:
    if type(x) is Nauczyciel and szukana == x.imie_nazwisko:
        nauczyciel = x
        break
if nauczyciel is not None:
    for x in szkoła:
        if type(x) is Wychowawca:
            for s in nauczyciel.sale:
                if s in x.sale:
                    print(x.nazwa)
                    break
    exit()

uczen = None
for x in szkoła:
    if type(x) is Uczen and szukana == x.imie_nazwisko:
        uczen = x
        break
if uczen is not None:
    for x in szkoła:
        if type(x) is Nauczyciel:
            if uczen.sala in x.sale:
                print(x.przedmiot, x.imie_nazwisko)
