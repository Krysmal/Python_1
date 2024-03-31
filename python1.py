zmienna = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
imie="krzysztof"
nazwisko="malinowski"
lit_1=imie[1]
lit_2=nazwisko[2]
il_1=zmienna.count(lit_1)
il_2=zmienna.count(lit_2)

print("W tekście jest "+str(il_1)+" liter "+lit_1+" oraz "+str(il_2)+" liter "+lit_2)


lista=[1,9,6,4,5,3,7,8,2,10]
print(lista)
lista2=lista[5:10].copy()
del lista[5:10]
print(lista,lista2)
lista_pol=lista+lista2
lista_sort=lista_pol.copy()
lista_sort.sort()
print(lista_pol)
print(lista_sort)
x="imię i nazwisko: Krzysztof Malinowski"
plik=open("C:/temp/KrzysztofMalinowskiLab02.txt", "w")
plik.write(x)
plik.close()