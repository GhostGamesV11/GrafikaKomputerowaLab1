from PIL import Image
import numpy as np


#zad 2
obrazek = Image.open("inicjaly.bmp")
# obrazek.show()
# print("---------- informacje o obrazie")
# print("tryb:", obrazek.mode)
# print("format:", obrazek.format)
# print("rozmiar:", obrazek.size)

#zad4
dane_obrazka = np.asarray(obrazek)
# print("---------------- informqcje o tablicy obrazu----------------")
# print("typ danych tablicy:", dane_obrazka.dtype)
# print("rozmiar tablicy:", dane_obrazka.shape)
# print("liczba elementow:", dane_obrazka.size)
# print("wymiar tablicy:", dane_obrazka.ndim)
# print("rozmiar wyrazu tablicy:",
#       dane_obrazka.itemsize)


#zad 3
# dane_obrazka1 = dane_obrazka * 1
# print(dane_obrazka1)
# ob_d = Image.fromarray(dane_obrazka)
#
# dane_text = open('inicjaly.txt', 'w')
# for rows in dane_obrazka1:
#     for item in rows:
#         dane_text.write(str(item) + ' ')
#     dane_text.write('\n')

#zad 4.2
# piksel1 = dane_obrazka[30][50]
# piksel2 = dane_obrazka[40][90]
# piksel3 = dane_obrazka[0][99]
# print("(50)(30) =", piksel1)
# print("(90)(40) =" , piksel2)
# print("(99)(0) =", piksel3 )

#zad 5
# t1  = np.loadtxt("inicjaly.txt", dtype=np.bool_)
# t2 = dane_obrazka
#
# print("typ danych tablicy t1:", t1.dtype)
# print("rozmiar tablicy t1 :", t1.shape)
# print("wymiar tablicy t1 :", t1.ndim)
#
# print("------------------------")
#
# print("typ danych tablicy t2:", t2.dtype)
# print("rozmiar tablicy t2 :", t2.shape)
# print("wymiar tablicy t2 :", t2.ndim)
#
#
# print("---- porównywanie tablic ------")
#
# porownanie = t1 == t2
# czy_rowne = porownanie.all()
# print("czy tablice sa równe? ", czy_rowne)



#zad 6

t1 = np.loadtxt("inicjaly.txt" , dtype=np.int_)
t2 = dane_obrazka


print("typ danych tablicy t1:", t1.dtype)
print("rozmiar tablicy t1 :", t1.shape)
print("wymiar tablicy t1 :", t1.ndim)

print("------------------------")

print("typ danych tablicy t2:", t2.dtype)
print("rozmiar tablicy t2 :", t2.shape)
print("wymiar tablicy t2 :", t2.ndim)


print("---- porównywanie tablic ------")

porownanie2 = t1 == t2
czy_rowne = porownanie2.all()
print("czy tablice sa równe? ", czy_rowne)


t1_text = open('tab1', 'w')
for rows in t1:
    for item in rows:
        t1_text.write(str(item) + ' ')
    t1_text.write('\n')





