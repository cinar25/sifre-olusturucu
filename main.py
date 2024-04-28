import random
karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
#input ifadesiyle kullanıcıdan bir string ifade alırız
uzunluk = int(input("şifre uzunluğunu giriniz:"))
sifre = " "
for i in range(uzunluk):
    sifre += random.choice(karakter)

print(f"{uzunluk} haneli şifrenizi oluşturulmuştur şifreniz: sifre{sifre}")