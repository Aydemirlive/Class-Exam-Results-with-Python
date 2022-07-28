import string
import csv
ogrencilist=[]
secim="y"
f = open("ogrenci.csv",'a',)
yazıcı=csv.writer(f)
while  secim=="y":
    ogrenciAdi=str(input("Öğrencinin adını giriniz:"))
    
    ogrenciSoyadi=str(input("Öğrencinin soyadını giriniz:"))    
    ogrenciNO=str(input("Öğrencinin numarasını giriniz:"))
    ogrenciPuan=str(input("Öğrencinin sınav puanını giriniz:"))
    if int(ogrenciPuan)>=80:
        harfnotu="A"
        yazıcı.writerow([ogrenciAdi,ogrenciSoyadi,ogrenciNO,ogrenciPuan,harfnotu])
    elif int(ogrenciPuan) >=60 and int(ogrenciPuan) <=79:
        harfnotu="B"
        yazıcı.writerow([ogrenciAdi,ogrenciSoyadi,ogrenciNO,ogrenciPuan,harfnotu])
    elif int(ogrenciPuan) >=40 and int(ogrenciPuan) <=59:
        harfnotu="C"
        yazıcı.writerow([ogrenciAdi,ogrenciSoyadi,ogrenciNO,ogrenciPuan,harfnotu])
    elif int(ogrenciPuan) >=20 and int(ogrenciPuan) <=39:
        harfnotu="D"
        yazıcı.writerow([ogrenciAdi,ogrenciSoyadi,ogrenciNO,ogrenciPuan,harfnotu])
    elif int(ogrenciPuan) >=0 and int(ogrenciPuan) <=19:
        harfnotu="F"
        yazıcı.writerow([ogrenciAdi,ogrenciSoyadi,ogrenciNO,ogrenciPuan,harfnotu])
    print("Evet ise y,Hayır ise n'ye basınız")
    secim=str(input("Yeni bir öğrenci girmek istiyor musunuz?"))
f.close
with open("ogrenci.csv") as dosyam:
  okuyucu = csv.reader(dosyam)
  for satir in okuyucu:
    print(satir)


