import sys
from ast import Break, Try, excepthandler
import mechanize
import requests
import responses

if sys.version_info[0] !=3:
    print("please follow the installation guide and do not omit any lines!!")

Break
print('\033[1;31m ___  ___  ___   _____  _      _____ ______\033[1;32m')
print('\033[1;31m |  \/  | / _ \ |_   _|| |    |  ___|| ___ \\033[1;32m')
print('\033[1;31m | .  . |/ /_\ \  | |  | |    | |__  | |_/ /\033[1;32m')
print('\033[1;31m | |\/| ||  _  |  | |  | |    |  __| |    / \033[1;32m')
print('\033[1;31m | |  | || | | | _| |_ | |____| |___ | |\ \ \033[1;32m')
print('\033[1;31m \_|  |_/\_| |_/ \___/ \_____/\____/ \_| \_|\033[1;32m')
                                           
                                           
print("ANONY MAILER BY CYBERNETICS ~ MADE BY AN HACKER FOR HACKERS")

br = mechanize.Browser()

to = input("Enter receivers mail address: ")
subject = input("Enter your message subject: ")
print ("Message: ")
message = input("Enter your message content: ")

url = "https://anonymouse.org/anonemail.html"
headers = "Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)"
br.addheaders = [('User-agent',headers)]
br.open(url)
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handler_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_debug_http(False)
br.set_debug_redirects(False)

br.select_form(nr=0)

br.form['To'] = to
br.form['Subject'] = subject
br.form['Message'] = message

result = br.submit()

response_data = responses.r()

if " The e-mail has been sent anonymously" in responses:
    print("\n The message has been successfully sent \n The recipient will get the message within 6hours!!! ")
else: 
    print('Failed to send message')
    print('\nPreparing an alternative module to fix issues.......\n')

excepthandler
 
ConnectionError
ConnectionRefusedError

Try
print('\n please check your wifi ~ cellular data connection\n then RESTART SOFTWARE!!')

sys.exit