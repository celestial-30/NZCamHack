import requests,re,os
import time
import sys
from os import system
from platform import platform
from time import sleep
import os
puk = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'

os.system(delet)
time.sleep(1)

print('------Version 1.2------\n')

time.sleep(4)
os.system(delet)
print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▀█░▄▄▀█░▄▀▄░██░██░█░▄▄▀█▀▄▀█░█▀██
██░████░▀▀░█░█▄█░██░▄▄░█░▀▀░█░█▀█░▄▀██
██░▀▀▄█▄██▄█▄███▄██░██░█▄██▄██▄██▄█▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")
print("Welcome to camera-hack!")
k = input("Press enter to begin...")
    

num = int(5)
if num == 5:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,5):
			
                url = ("https://www.insecam.org/en/bycountry/NZ/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]
                     print (hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")             

        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,6):
			
                url = ("https://www.insecam.org/en/bycountry/CO/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ") 


print("Ready! Logs saved in logs.txt")
print("""

Modified for use in NZ by Marengo (known as Celestial-30 on GH)
Email: lithium8@protonmail.com

This software is based on WebHack by yan4kyt on github, I only streamlined its use. (2/3 of the code was a banner animation.) if you want to support this software by them a coffee :)
------Version 1.0------
""")
