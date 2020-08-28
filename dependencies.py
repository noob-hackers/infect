#!usr/bin/env/python

import os
import time

Y = set(['yes', 'y', 'YES', 'Y'])
N = set(['no', 'n', 'NO', 'N'])

os.system("apt install figlet")
os.system("figlet INSTALLATION")
os.system("clear")
agree = input("This tool needs some depedencies are you sure you want to install it Y / N ")

def agreement():
  if agree in Y:
    os.system("figlet INSTALLING THE DEPENDENCIES")
    time.sleep(0.5)
    os.system("apt update")
    os.system("apt upgrade")
    os.system("pkg upgrade")
    os.system("pkg install git")
    os.system("pkg install python -y")
    os.system("pip install lolcat")
    os.system("clear")
    os.system("figlet INSTALLATION COMPLETED...")
    print("you can now run infect.sh")
  elif agree in N:
    print("This tool needs some depedencies please run python3 dependencies.py")
    print("exiting")
    exit()
    
agreement()   
