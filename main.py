import telebot
import os
import requests
from bs4 import BeautifulSoup as bs

my_secret = os.environ['apiTelegramBot']

bot = telebot.TeleBot(my_secret, parse_mode=None)

kode = {
'0': ' Cerah / Clear Skies',
'1': ' Cerah Berawan / Partly Cloudy',
'2': ' Cerah Berawan / Partly Cloudy ',
'3': ' Berawan / Mostly Cloudy',
'4': ' Berawan Tebal / Overcast ',
'5': ' Udara Kabur / Haze ',
'10': ' Asap / Smoke',
'45': ' Kabut / Fog',
'60': ' Hujan Ringan / Light Rain',
'61': ' Hujan Sedang / Rain',
'63': ' Hujan Lebat / Heavy Rain ',
'80': ' Hujan Lokal / Isolated Shower',
'95': ' Hujan Petir / Severe Thunderstorm',
'97': ' Hujan Petir / Severe Thunderstorm'
}

cuaca = {
  'pagi' : '',
  'siang' : '',
  'malam' : '',
}

def dataCuacaLumajang_def() :
  dataJatimAPI = requests.get("https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-JawaTimur.xml")
  dataJatim = dataJatimAPI.text
  soup = bs(dataJatim, 'xml')
  dataCuacaLumajang = soup.find(id="501286").find(id="weather")

  dataCuacaLumajangH0 = dataCuacaLumajang.find(h="0").value.text 
  dataCuacaLumajangH6 = dataCuacaLumajang.find(h="6").value.text
  dataCuacaLumajangH12 = dataCuacaLumajang.find(h="12").value.text

  cuaca['pagi'] = kode[dataCuacaLumajangH0]
  cuaca['siang'] = kode[dataCuacaLumajangH6]
  cuaca['malam'] = kode[dataCuacaLumajangH12]
  
  prakiraan = str(
    "Cuaca Hari ini" + 
    "\n pagi" + cuaca['pagi'] +
    "\n pagi" + cuaca['siang'] +
    "\n pagi" + cuaca['malam'] 
    )

  return prakiraan

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, 'WELCOME MTHEFAKEE!')

@bot.message_handler(commands=['cuaca'])
def send_welcome(message):
	bot.reply_to(message, dataCuacaLumajang_def())


bot.polling()

