import requests
import re
import webbrowser
import time

girilen=input("lütfen hesap linkini giriniz: ")
#girilen linki "girilen" isimli değişkene atadık

pattern ="https://i.scdn.co/image/\w*"   #kaynak kodları içinde arayacağımız kalıp
try:
    response = requests.get(girilen).text
#sayfanın kaynak kodlarını "response" değişkenine atadık

    konumlar=re.search(pattern,response)
#kalıbımızı kaynak kodların içinde arıyoruz

except:
    print("URL error")
    time.sleep(10)
    exit()

try:
    webbrowser.open(response[konumlar.span()[0] : konumlar.span()[1]])
#kodların içinde bulunan aralığı tarayıcıda açmayı denedik

except:
    print("link bulunamadı")
    time.sleep(10)
#başarısız olursa ekrana uyarı döndürdük