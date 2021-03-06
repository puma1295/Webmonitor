### Import Lihraries ###
import urllib
import time
import datetime
from win10toast import ToastNotifier

### Banner ###
banner = ("#################################\n"
          "##    VORONINA WEBMONITOR      ##\n"
          "##  Coded By: Polina Voronina  ##\n"
          "#################################")
print(banner)
print('')

### Definitions ###
toaster = ToastNotifier()
target = raw_input("(Example: https://www.google.com)\nURL: ") # This will ask for the URL
print("\n")
status = urllib.urlopen(str(target)).getcode()

### Start of main Code ###

def function():
    if "200" in str(status):
        print ("[+] ONLINE - " + str(status) + " - " + str(datetime.datetime.now())+"\n")
    else:
        print ("[+] OFFLINE - " + str(status) + " - "  + str(datetime.datetime.now()) + "\n")
        toaster.show_toast("VORONINA WEBMONITOR", "DOMAIN: " + str(target) + "\n" + "STATUS: DOWN\n" + "STATUS CODE: " + str(status))
        print('[!] Quitting...')
        exit(0)
    time.sleep(3) # This will make the application wait 3 seconds before it checks the domain again

while True:
    function() # This is for an infinite loop
