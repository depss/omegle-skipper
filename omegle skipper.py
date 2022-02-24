import ctypes
import os
import time
from colorama.ansi import Fore
import pyautogui
from colorama import init, Fore

init()
ctypes.windll.kernel32.SetConsoleTitleW('Omegle Skipper By depss')

tag = (Fore.YELLOW + ''' ██████╗ ███╗   ███╗███████╗ ██████╗ ██╗     ███████╗    ███████╗██╗  ██╗██╗██████╗ ██████╗ ███████╗██████╗ 
██╔═══██╗████╗ ████║██╔════╝██╔════╝ ██║     ██╔════╝    ██╔════╝██║ ██╔╝██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║   ██║██╔████╔██║█████╗  ██║  ███╗██║     █████╗      ███████╗█████╔╝ ██║██████╔╝██████╔╝█████╗  ██████╔╝
██║   ██║██║╚██╔╝██║██╔══╝  ██║   ██║██║     ██╔══╝      ╚════██║██╔═██╗ ██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
╚██████╔╝██║ ╚═╝ ██║███████╗╚██████╔╝███████╗███████╗    ███████║██║  ██╗██║██║     ██║     ███████╗██║  ██║
 ╚═════╝ ╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚══════╝╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
-------------------------------------------------------------------------------------------------------------
Written by: depss#3615''')

def banner():
    os.system('cls')
    print(tag)
banner()

def main():
    print()
    run_skipper = input(Fore.LIGHTBLUE_EX + 'Would you like to skip and send messages automatically?[Y/N]: ')
    if run_skipper == 'Y':
        pass
    elif run_skipper == 'N':
        banner()
        print()
        print(Fore.RED + 'Exiting in 5 Seconds')
        time.sleep(5)
        exit()
    else:
        banner()
        print()
        print(Fore.RED + 'Error Y/N must be capitilized in order to funciton!')
        print()
        print('Exiting in 5 Seconds')
        time.sleep(5)
        exit()

main()

msg_limit = 101

banner()
print()
try:
    skips = int(input(Fore.LIGHTBLUE_EX + 'How many times would you like to skip?: '))
except ValueError:
    banner()
    print()
    print(Fore.RED + 'Error must be a number, exiting in 5 seconds')
    time.sleep(5)
    exit()
    
print()
msg = input('What is the message you would like to send?: ')

if len(msg) > msg_limit:
    print('Error message must be less 100 characters or less!')
else:
    pass

def skipper():
    banner()
    print()
    print(Fore.LIGHTBLUE_EX + 'Press enter when omegle is open to the video page and you are ready (Note: be on the video page but not in a video chat)')
    os.system('pause')

    banner()
    print()
    print(Fore.GREEN + 'Skipping and auto message starting in 10 seconds!')
    time.sleep(10)

    for x in range(skips):
        pyautogui.press('Escape')
        pyautogui.press('Escape')
        time.sleep(3)
        pyautogui.typewrite(msg, interval=.05)
        pyautogui.press('Enter')
        time.sleep(5)

    banner()
    print()
    print(Fore.GREEN + 'Process finished succesfuly, exiting in 5 seconds!')
    time.sleep(5)
    exit()
skipper()
