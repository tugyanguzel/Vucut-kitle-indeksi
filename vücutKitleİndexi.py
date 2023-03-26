kilo = float(input("Lütfen kilonuzu giriniz:"))
boy = int(input("Lütfen boy uzunluğunuzu girini:"))

print("-" * 60)
vki=kilo/((boy/100)**2)
print("VÜCUT KİTLE İNDEXİ DEĞERİ: " ,vki)
print("-" * 60)

if vki < 19 :
    print("ZAYIF")

elif 19 < vki < 24.9:
    print("NORMAL")

elif 25 < vki < 29.9:
    print("HAFİF ŞİŞMAN")

elif 30 < vki < 34.9:
    print("ŞİŞMAN") 
    
elif vki > 35:
    print("OBEZ")
