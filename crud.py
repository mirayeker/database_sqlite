import sqlite3
con = sqlite3.connect("kütüphane.db") #connection isimli bir değişken oluşturduk
cursor=con.cursor() #imleç oluşturduk


def tablo_olustur() :
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık(İsim TEXT, Yazar TEXT, Yayınevi TEXT,Sayfa_Sayısı INT)") #calıştır anlamına gelen execute oluşturduk
    con.commit() #işlem yapabilmek için yazmak zorundayız


#manuel olarak veri eklersek:

def veri_ekle():
    cursor.execute("INSERT INTO kitaplık values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()


#kullanıcıdan verileri alıp eklersek:

def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()

#kitaplık database'den tüm kitapları alırsak:

def verileri_al():
    cursor.execute("Select *From kitaplık")
    liste = cursor.fetchall()  # cursorun üzerindeki işlemleri dönüp listeye atar.
    # con.commit yapmadık çünkü herhasngi bir güncelleme yapmıyoruz bilgileri alıyoruz.
    # print(liste) #liste içinde  demetler olarak biliyor
    # daha güzel şekilde şöyle alabilirz
    for i in liste:
        print(i)
#isim ve yazar bilgilerini almak istersek:

def verileri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık")
    liste=cursor.fetchall()
    print("kitaplık tablosunun bilgileri")
    for i in liste:
        print(i)

#yayınevi bilgilerini almak istersek:

def verileri_al3(yayınevi):
    cursor.execute("Select * From kitaplık where Yayınevi = ? ",(yayınevi,))
    liste=cursor.fetchall()
    print("Kitaplık tablosunun bilgileri")
    for i in liste:
        print(i)


#yayınevini güncellersek :
def verileri_guncelle(eski_yayınevi,yeni_yayınevi):
    cursor.execute("Update kitaplık set Yayınevi = ? where Yayınevi =?",(yeni_yayınevi,eski_yayınevi))
    con.commit()

#veriyi yazara göre silmek istersek :
def verileri_sil(yazar):
    cursor.execute("Delete From kitaplık where Yazar =? ",(yazar,))
    con.commit()



isim=input("isim:")
yazar=input("yazar:")
yayınevi=input("yayın evi:")
sayfa_sayısı=int(input("Sayfa Sayısı:"))

#tablomuzu olusturalım dersek:
tablo_olustur()

#verilerimizi ekleyelim dersek :
veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı)

#eklediğimiz verileri görelim dersek:
verileri_al()
verileri_al2()
verileri_al3("mirisko")

#databasemizi güncelleyelim dersek:
verileri_guncelle("mirisko","mavi")
verileri_al()

#verilerimizi silelim dersek:
verileri_sil("mermaid")
verileri_al()


con.close() #bağlantıyı kapatmamız gerekir