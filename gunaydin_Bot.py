import pywhatkit
import datetime
import time
import random

def random_msg(): # Random Mesaj için hazırlanmış Array barındıran Fonksiyon
    msgs = ["Günaydın sevgilim. Uyanır uyanmaz gelirsin aklıma, bir güneşe bakarım bir de bana gülen fotoğrafına.",
    "Günaydın birtanem. Mutlulukların aşkımızla bütünleştiği, üzüntülerin kıyılarımıza ulaşmadığı, aşkın en güzel halinin bize yakıştığı güzel bir güne merhaba diyelim mi?",
    "Günaydın biriciğim. Nasıl ki çiçekler sever doğayı, nasıl ki dünya sever evreni, nasıl ki gökyüzü sever yıldızları... İşte ben de seni bu devasa şekilde öyle severim. Sen benim canımsın! Ruhumun sahibi, huzurumun sebebisin.",
    "Günaydın biricik aşkım. Sabah olsun diye herkes güneşin doğmasını beklerken, zavallı güneş de senin uyanmanı bekliyor!",
    "Günaydın gün ışığım! Her günün ayrı bir güzelliği olsun, güne gülerek başla sevgilim.",
    "Günaydın sevgilim. Güneş kadar aydınlık, gözlerin kadar güzel, sözlerin gibi kusursuz bir güne merhaba demenin tam zamanı!",
    "Günaydın aşkım. Seni sevmek güneşe dokunmak gibi, sana bakınca eriyor içimdeki buz kütleleri. Her günüm seninle başlar, seninle daha da güzel hayat.",
    "Günaydın nur yüzlüm. Rüyalarımın sahibi sensin. Uykumdan uyanınca adın yankılanır odamda. Sabah güneşi usulca doğarken, bu mesajı yolluyorum sana…",
    "Güneşin doğuşu gibi güzel ve aydınlık olmasını dilerim.",
    "Bugünün sana keyifli ve huzurlu bir gün olmasını umarım.",
    "Bugünün senin için özel ve anlamlı olmasını dilerim.Günaydın",
    "Her gün olduğu gibi bugün de seni düşündüm ve seni çok sevdiğimi hatırlatmak istedim.",
    "Bugünün güneşli ve huzurlu bir gün olmasını dilerim. Seni her zaman yanımda hissetmemi sağla.",
    "Seninle başlamak istediğim bu gün, benim için çok anlamlı ve özeldir.",
    "Hayatımın en güzel günlerinden biri bugündür çünkü sen varsın. Günaydın!",
    "Seni her zaman güne enerjik ve pozitif bir şekilde başlamanı dilerim. Bugün de seni düşünerek güne başladım."]

    rand_num = random.randint(0, len(msgs))

    return msgs[rand_num]

to_number = "+905535764453" # Gönderilecek kişinin numarası
send_time = "08:30"         # Gönderilecek Saat
msg = random_msg()          # Gönderilecek Mesaj

send_time_hour = int(send_time.split(":")[0])
send_time_minute = int(send_time.split(":")[1])

send_time_ = datetime.datetime.now().replace(hour=send_time_hour,minute=send_time_minute,second=0,microsecond=0)

if send_time_ < datetime.datetime.now():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    send_time_ = datetime.datetime.combine(tomorrow, datetime.time(send_time_hour,send_time_minute))

later_1min = send_time_ + datetime.timedelta(minutes=1)

while True:
    now = datetime.datetime.now()
    if now.hour == send_time_hour and now.minute == send_time_minute and now.day == send_time_.day:
        pywhatkit.sendwhatmsg(to_number,msg,send_time_hour,send_time_minute+1)
        print(f"Mesaj Gönderildi - {now}")

        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        send_time_ = datetime.datetime.combine(tomorrow, datetime.time(send_time_hour,send_time_minute))
        later_1min = send_time_ + datetime.timedelta(minutes=1)
    
    #time.sleep(60)