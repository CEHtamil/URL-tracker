import requests
import sys
from colorama import Fore, Back, Style

class name_ban:
    def banner(self):
        c = Fore.WHITE
        a = Fore.YELLOW
        b = Fore.RED
        d = Fore.GREEN
        e = Fore.BLUE
        print(d + " ▒██▀███  ▒█████ ▒██  ██  ")
        print(a + " ▒██      ▒█   ▀ ▒██  ██  ")
        print(b + " ▒██      ▒███   ▒██████  ")
        print(e + " ▒██  ▄▄  ▒█   ▄ ▒██  ██  ")
        print(c + " ▒██████  ▒█████ ▒██  ██  ")
        print(c + " ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒░░  ▒  ")
        print(b + "Coded by:VISHVA-Ethical-Hacker")
        print(c + "░  ░▒ ░ ▒░ ░ ░  ░   ▒  ▒ ▓")
        print(a + "CEH தமிழ் CEH தமிழ் CEH தமிழ்")
        print(c + "░▒ ░▓ ▒ ▒░ ░ ▒  ░   ▒  ▒ ░")

    def help(self):
        print('url-tracker 1.0')
        about = '''Have you ever wondered: Where does this link go? 
this tool is allows you to see the complete path a redirected URL goes through. 
It will show you the full redirection path of URLs, shortened links, or tiny URLs.'''
        print(about)
        print('\nRequirements: Python 3, requests and colorama libraries')
        print('To install the requirements run these commands')
        print('\tUpdate: apt-get update')
        print('\tPython 3: apt-get install python3')
        print('\tRequests: pip install requests')
        print('\tcolorama: pip install colorama')
        print('\nRun the tool: url-tracker.py --track')
        print('Commands')
        print("--track or -t  -> Track the given URL's redirection path & find its end URL.")
        print('--help or -h  -> To display helpline how to use this tool & about tool. ')
        print('\nCoded by: VISHVA Ethical-Hacker')
        print('Subscribe YouTube : https://www.youtube.com/channel/UCxvjPSdX6aBMB55Fci2cJSw')

    def cmdusage(self):
        print('Invalid command-line arguments!')
        print('Commands')
        print("--track or -t  -> Track the given URL's redirection path & find its end URL.")
        print('--help or -h  -> To display helpline how to use this tool & about tool. ')
        print('\nCoded by: VISHVA Ethical-Hacker')

class redli:
    def __init__(self, url):
        self.url = url
    def track_url(self):
        try:
            resp = requests.get(self.url)
            if resp.history:
                print(Fore.RED + '\nYes URL is Redirected or Shorten!')
                print(Fore.RED + 'Here the following redirected chain...\n')
                for r in resp.history:
                    print(Fore.RED + '|', r.status_code, '|', r.url, '|', r.reason)
                print(Fore.BLUE + '\nEND URL :', resp.url)
                print(Fore.WHITE + 'Status Code :', resp.status_code, resp.reason)
                print('\nCoded by: VISHVA Ethical-Hacker')
            else:
                print(Fore.WHITE + '\nURL is Not Redirected or Shorten!')
                print(Fore.BLUE + 'END URL :', resp.url)
                print(Fore.WHITE + 'Status Code :',resp.status_code, resp.reason)
                print('\nCoded by: VISHVA Ethical-Hacker')
        except BaseException as be:
            print(Fore.RED + 'Tracking Failed! Check URL')
            print(be)
            exit()

if __name__=='__main__':
    intro = name_ban()
    intro.banner()
    e = Fore.BLUE
    if len(sys.argv) == 2:
        if sys.argv[1] == '--help' or sys.argv[1] == '-h':
            intro.help()
        elif sys.argv[1] == '--track' or sys.argv[1] == '-t':
            url = input(e + "Enter URL to Track:")
            print('Tracking Redirection Of URL...')
            print('\nCoded by: VISHVA Ethical-Hacker')
            track = redli(url)
            track.track_url()
        else:
            intro.cmdusage()
    else:
        intro.cmdusage()
