# Görev 2: Verilen string ifadenin tüm harflerini büyük harfe
# çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime
# ayırınız.

# İpucu: String methodlarını kullanınız.
##########################################################
text = "The goal is to turn data into information, and information into insight."

text.upper().replace(",", " ").replace(".", " ").split()
##########################################################
# Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Adım 1: Verilen listenin eleman sayısına bakınız.

len(lst)

# Adım 2: Sıfırıncı ve onuncu indesteki elemanları çağırınız.

print(lst[0], lst[10])

# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz

data = [lst[:4]]

# Adım 4: Sekizinci indeksteki elemanı siliniz.

lst.pop(8)
# Adım 5: Yeni bir eleman ekleyiniz.

lst.append("J")

# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst.insert(8, "N")

#########################################################

# Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

##########################################################

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}
# Adım 1: Key değerlerine erişiniz.

dict.keys()

# Adım 2: Value'lara erişiniz.

dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak günceleyiniz.

dict["Daisy"][1] = 13

# Adım 4: Key değeri Ahmet, value değeri ["Turkey", 24] olan yeni bir değer ekleyiniz.

dict["Ahmet"] = ["Turkey", 24]

# Adım 5: Antonio'yu dictionary'den siliniz.

del dict["Antonio"]

###############################################################
# Görev 5: Argüman olarak bir liste alan, listenin içerisindeki
# tek ve çift sayıları ayrı listelere atayan ve bu listeleri
# return eden fonksiyonu yazınız.

# İpucu: Liste elemanlarına tek tek erişmeniz gerekmektedir.
# İpucu: Her bir eleman çift veya tek olma durumunu
# kontrol etmek için % yapısını kullanabilirsiniz.
##############################################################

num_l = [2, 13, 18, 93, 22]



def oddOrEven(num_lst):
    even_list1 = []
    odd_list1 = []
    for i in num_lst:
        if i % 2 == 0:
            even_list1.append(i)
        else:
            odd_list1.append(i)
    return even_list1, odd_list1


even_list1, odd_list1 = oddOrEven(num_l)
print(even_list1, odd_list1)
##########################################################
# Görev 6: List Comprehension yapısı kullanarak car_crashes
# verisindeki numeric değişkenlerin isimlerini büyük harfe
# çeviriniz ve başına NUM ekleyiniz

# İpucu: Numeric olmayan değişkenlerin de isimleri büyümeli.
# İpucu: Tek bir list comprehension yapısı kullanılmalı.
##########################################################

import seaborn as sns

df1 = sns.load_dataset("car_crashes")
df1.columns

df1.columns = ["NUM_" + i.upper() if df1[i].dtype != "O" else i.upper() for i in df1.columns]
df1.columns


##########################################################
# Görev 7: List Comprehension yapısı kullanarak car_crashes
# verisindeki isminde "no" BARINDIRMAYAN değişkenlerin sonuna
# "FLAG" yazınız.

# İpucu: Tüm değişkenlerin isimleri büyük harf olmalı.
# İpucu: Tek bir list comprehension yapısı kullanılmalı.
##########################################################

df3 = sns.load_dataset("car_crashes")
df3.columns
df3.columns = [i.upper() + "_FLAG" if "no" not in i else i.upper() for i in df3.columns]
print(df3.columns)

##########################################################
# Görev 8: List Comprehension yapısı kullanarak aşağıda verilen
# değişken isimlerinden FARKLI olan değişkenlerin

# İpucu: Önce verilen listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# İpucu: Sonra df[new_cols] ile bu değişkenleri seçerek yeni birdf oluşturunuz ve adını new_df olarak isimlendiriniz.
##########################################################


import seaborn as sns

df4 = sns.load_dataset("car_crashes")
df4.columns
og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df4.columns if col not in og_list]
df_new = df4[new_cols]

