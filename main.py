import time
import webbrowser
import os
import json
import sys
import requests
import mechanize
from colorama import Fore, Style, init

init()

authenticated = False

def login():
    global authenticated
    print("\033[91m[>] Welcome to joshua's' tool!")
    username = input("\033[91m[>] Enter username: ")
    password = input("\033[91m[>] Enter password: ")

    if username == "admin" and password == "admin":
        authenticated = True
        print("\n\033[92mLogin successful.\033[0m")
    else:
        print("\n\033[1;91mInvalid username or password.\033[0m")
        time.sleep(2)
        os.system('clear' if os.name == 'posix' else 'cls')

def print_logo_in_box(text):
    max_length = max(len(line) for line in text)
    box_width = max_length + 6
    box_height = len(text) + 2

    print(Fore.BLUE + "〖-" * (box_width // 2) + "" + Style.RESET_ALL)

    for line in text:
        padding = (max_length - len(line)) // 2
        print(Fore.BLUE + " " * 2 + Style.RESET_ALL + Fore.GREEN + " " * padding + line + " " * (max_length - len(line) - padding) + " " * 2 + Style.RESET_ALL)

    print(Fore.BLUE + "〖-" * (box_width // 2) + "" + Style.RESET_ALL)

def show_options(options):
    print(Fore.BLUE + "\nOptions:" + Style.RESET_ALL)
    for key, value in options.items():
        print(Fore.BLUE + key + ": " + value + Style.RESET_ALL)

def sendSpam(user, message):
    url = 'https://ngl.link/api/submit'
    payload = {'username': user, 'question': message, 'deviceId': ""}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code

def execute_option_1():
    user = input("\033[91m[*] Enter username: \033[1;91m")
    message = input("\033[91m[*] Enter message: \033[1;91m")
    amount = int(input("\033[91m[*] Enter amount: \033[1;91m"))
    
    if amount > 999:
        print("Sorry, the limit is 999.")
    else:
        for i in range(1, amount + 1):
            status_code = sendSpam(user, message)
            text = f"\033[93m[ NGL ] \033[91m[\033[91m{i}\033[91m][{'success' if status_code == 200 else 'error'}]: Message sent to target: {user}\033[0m"
            print(text)
            time.sleep(2)
        time.sleep(3)
        os.system('clear' if os.name == 'posix' else 'cls')  
        main()

def execute_option_2():
    token()

def token():
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [("User-Agent", "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")]

    def EAAAAU(user, passw):
        res = br.open(f"https://b-api.facebook.com/method/auth.login?email={user}&password={passw}&format=json&generate_session_cookies=1&generate_machine_id=1&generate_analytics_claim=1&locale=en_US&client_country_code=US&credentials_type=device_based_login_password&fb_api_caller_class=com.facebook.account.login.protocol.Fb4aAuthHandler&fb_api_req_friendly_name=authenticate&api_key=882a8490361da98702bf97a021ddc14d&access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32")
        data = json.load(res)
        if 'access_token' in data:
            return data['access_token']
        else:
            return "\033[1;91m  ERROR: \033[0m\033[91m" + data["error_msg"]

    def EAADYP(user, passw):
        res = br.open(f"https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email={user}&locale=en_US&password={passw}&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm")
        data = json.load(res)
        if 'access_token' in data:
            return data['access_token']
        else:
            return "\033[1;91mERROR: \033[0m\033[91m" + data["error_msg"]

    try:
        user = input("  \033[1;97mUSERNAME:\033[91m~ ")
        passw = input("  \033[97mPASSWORD:\033[91m~ ")
        print(f" \n[EAAAAU]: \033[92m{EAAAAU(user,passw)}\n \n[EAADYP]: \033[92m{EAADYP(user,passw)}")
        print()
        input("  \033[0m\033[90mEnter >>")
        os.system('clear' if os.name == 'posix' else 'cls')  
        main()
    except Exception as e:
        print("\n  ERROR: While getting your access token:", e)
        sys.exit()

def main():
    global authenticated
    if not authenticated:
        login()

    if authenticated:
        os.system('clear' if os.name == 'posix' else 'cls')

        if os.environ.get('FIRST_RUN', '1') == '1':
            webbrowser.open("https://www.facebook.com/profile.php?id=100088690249020")
            os.environ['FIRST_RUN'] = '0' 

        logo_text = [
            "██████╗░██╗░░░██╗██╗░░██╗███████╗",
            "██╔══██╗██║░░░██║██║░██╔╝██╔════╝",
            "██████╔╝██║░░░██║█████═╝░█████╗░░",
            "██╔═══╝░██║░░░██║██╔═██╗░██╔══╝░░",
            "██║░░░░░╚██████╔╝██║░╚██╗███████╗",
            "╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝╚══════╝"
        ]

        print_logo_in_box(logo_text)
        print(Fore.GREEN + "GitHub: https://github.com/joshuapostol")
        print(Fore.GREEN + "Facebook: joshua Apostol")
        print(Fore.GREEN + "Created by Joshua Apostol" + Style.RESET_ALL)

        options = {
            Fore.BLUE + "1": "NGL SPAM",
            Fore.BLUE + "2": "Get Facebook Access Token"
        }
        show_options(options)

        choice = input(Fore.BLUE + "Enter your choice: " + Style.RESET_ALL)
        if choice == "1":
            execute_option_1()
        elif choice == "2":
            execute_option_2()
        else:
            print(Fore.RED + "Invalid choice" + Style.RESET_ALL)
    else:
        login()

if __name__ == "__main__":
    main()