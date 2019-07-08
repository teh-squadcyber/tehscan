#!/usr/bin/python
#TEH Squad Cyber {CoDay#`XploiY}

import os
import sys
import requests

os.system ('pkg install curl -y')
os.system ('clear')
os.system ('sleep 3')
tgt = """\033[1;30;40m
[+]-----------------------------------[+]
 | MASUKAN TARGET TANPA HTTP/HTTPS/WWW |"""
print tgt
off = raw_input ("[SELECT#TARGET]> ")
os.system ('sleep 5 && clear')
teh = """\033[1;33;40m
           __    __    __    __
          /  \  /  \  /  \  /  \

_________/  __\/  __\/  __\/  __\__________
________/  /__/  /__/  /__/  /_____________)
        | / \   / \   / \   / \  \____
        |/   \_/   \_/   \_/   \    o \

  \033[0;31;47m{Web ScannerV1} TEHSQUADCYBER \033[1;33;40m\_____/--<
       \033[0;31;47m[INSTAGRAM : TEHSQUADCYBER.ID]"""
menu = """
\033[0;31;47m[1 ]\033[1;33;40m Traceroute
\033[0;31;47m[2 ]\033[1;33;40m Tes Ping
\033[0;31;47m[3 ]\033[1;33;40m Pencarian DNS
\033[0;31;47m[4 ]\033[1;33;40m Membalikkan DNS
\033[0;31;47m[5 ]\033[1;33;40m Temukan Host DNS
\033[0;31;47m[6 ]\033[1;33;40m Temukan DNS Bersama
\033[0;31;47m[7 ]\033[1;33;40m Transfer Zona
\033[0;31;47m[8 ]\033[1;33;40m Pencarian Whois
\033[0;31;47m[9 ]\033[1;33;40m Pencarian Lokasi IP
\033[0;31;47m[10]\033[1;33;40m Reverse IP Lookup
\033[0;31;47m[11]\033[1;33;40m Pemindaian Port TCP
\033[0;31;47m[12]\033[1;33;40m Pencarian Subnet
\033[0;31;47m[13]\033[1;33;40m Periksa Judul HTTP
\033[0;31;47m[14]\033[1;33;40m Ekstrak Tautan Halaman
\033[0;31;47m[15]\033[1;33;40m Keluar"""
os.system ('clear')
print teh
print menu
opt = input ("[rootXoption]> ")
if opt == 1:
   com = "https://api.hackertarget.com/mtr/?q=" + off
   request = requests.get(com)
   finish = request.text
   os.system ('clear')
   print teh
   print (finish)
elif opt == 2:
   com = "https://api.hackertarget.com/nping/?q=" + off
   request = requests.get(com)
   finish = request.text
   os.system ('clear')
   print teh
   print (finish)
elif opt == 3:
   com = "https://api.hackertarget.com/dnslookup/?q=" + off
   request = requests.get(com)
   finish = request.text
   os.system ('clear')
   print teh
   print (finish)
elif opt == 4:
   com = "https://api.hackertarget.com/reversedns/?q=" + off
   request = requests.get(com)
   finish = request.text
   os.system ('clear')
   print teh
   print (finish)
elif opt == 5:
   com = "https://api.hackertarget.com/hostsearch/?q=" + off
   request = requests.get(com)
   finish = request.text
   os.system ('clear')
   print teh
   print (finish)
elif opt == 6:
   com = "https://api.hackertarget.com/findshareddns/?q=" + off
   request = requests.get(com)
   finish = request.text
   os.system ('clear')
   print teh
   print (finish)
elif opt == 7:
   com = "https://api.hackertarget.com/zonetransfer/?q=" + off
   request = requests.get(com)
   finish = request.text
   os.system ('clear')
   print teh
   print (finish)
elif opt == 8:
   com = "https://api.hackertarget.com/whois/?q=" + off
   request = requests.get(com)
   finish = request.text
   os.system ('clear')
   print teh
   print (finish)
elif opt == 9:
   com = "https://api.hackertarget.com/geoip/?q=" + off
   request = requests.get(com)
   finish = request.text
   os.system ('clear')
   print teh
   print (finish)
elif opt == 10:
   com = "https://api.hackertarget.com/reverseiplookup/?q=" + off
   request = requests.get(com)
   finish = request.text
   os.system ('clear')
   print teh
   print (finish)
elif opt == 11:
   com = "https://api.hackertarget.com/nmap/?q=" + off
   request = requests.get(com)
   finish = request.text
   os.system ('clear')
   print teh
   print (finish)
elif opt == 12:
   com = "https://api.hackertarget.com/subnetcalc/?q=" + off
   request = requests.get(com)
   finish = request.text
   os.system ('clear')
   print teh
   print (finish)
elif opt == 13:
   com = "https://api.hackertarget.com/httpheaders/?q=" + off
   request = requests.get(com)
   finish = request.text
   os.system ('clear')
   print teh
   print (finish)
elif opt == 14:
   com = "https://api.hackertarget.com/pagelinks/?q=" + off
   request = requests.get(com)
   finish = request.text
   os.system ('clear')
   print teh
   print (finish)
elif opt == 15:
    os.system ('clear')
    print teh
    exit()

