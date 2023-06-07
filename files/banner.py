import os

logo = f"""

█░█ ▄▀█ █▀▄▀█ ▄▀█ ▄█ █▀▀   █░█ █ █▀█ █░█ █▀
█▀█ █▀█ █░▀░█ █▀█ ░█ █▄▄   ▀▄▀ █ █▀▄ █▄█ ▄█                                     
                                               
"""

from files.colors import *


def banner():
    print(ran + logo)

    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX,  "- " * 4, " [+] la computery xot naday , ayswteny ", "- " * 4 + ran + "|")
    print(ran +"\n", "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX,  "- " * 4, " [+] batawy teky ada", "- " * 4+ran + "|")
    print(ran +"\n", "|"+ Style.BRIGHT + Fore.LIGHTRED_EX,  "- " * 4, "[+] dway formatish wak peshtry lenayatawa ", "- " * 3+ran + "|")


def banner2():


    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX,  "- " * 4, " [+] la computery xot naday , ayswteny", "- " * 4 + ran + "|")
    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] batawy teky ada ", "- " * 4+ran + "|")
    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTRED_EX,  "- " * 4, "[+] dway formatish wak peshtry lenayatawa ", "- " * 3+ran + "|")

def clear():
    os.system("clear")
