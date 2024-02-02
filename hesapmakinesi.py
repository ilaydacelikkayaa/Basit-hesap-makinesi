#Pythonda basit hesap makinesi yapımı
def topla(x,y):
 return x+y
def cikar(x,y):
 return x-y
def bolme(x,y):
 return x/y
def carp(x,y):
 return x*y
print("yapmak istediginiz islemi secin")
print("1-toplama \n 2-cikarma \n 3-bolme \n 4-carpma")
secim=input("secimini gir:")
x=float(input("1.sayiyi gir:"))
y=float(input("2.sayiyi gir:"))
if secim=='1':
 print(x,"+",y,"=",topla(x,y))
elif secim=='2':
 print(x,"-",y,"=",cikar(x,y))
elif secim=='3':
 if y==0:
  print("bir sayi sifira bolunemez")
 else:
  print(x,"/",y,"=",bol(x,y))
elif secim=='4':
 print(x,"*",y,"=",carp(x,y))
else:
 print("gecersiz secim")