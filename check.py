import os, sys, mechanize, re
from requests.exceptions import ConnectionError

DEFAULT = "\033[0;37m"
DG = "\033[1;30m"
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
B = "\033[1;34m"
M = "\033[1;35m"
C = "\033[1;36m"
W = "\033[1;37m"

try:
   os.mkdir("output")
except:
   pass

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def banner():
   os.system("clear")

   print W +"  ___    ___ "
   print " ( _<    >_ ) "
   print " //        \\\ "
   print " \\\___..___// "
   print W +"  `-(    )-'         "+R+"{ "+W+"YAHOO MASS CHECKER "+R+"} "
   print W +"    _|__|_ "
   print "   /_|__|_\ "
   print "   /_|__|_\ "
   print "   /_\__/_\ "
   print W +"    \ || /  _)       "+R+"[ "+W+"Coded by  "+R+": "+Y+"Syahrul    "+R+"] "
   print W +"      ||   ( )       "+R+"[ "+W+"Subscribe "+R+": "+W+"Mbah Beluk "+R+"] "
   print W +"      \\\___// "
   print "       `---' "
   print "             "


def yahoolist():

    files = raw_input('Your file ' + R + '> '+ W)
    try:
         total = open(files, 'r').readlines()
    except IOError:
         print R + '['+ W +'!'+ R +'] '+ W +'File not found'
         exit()

    save = open('output/invalid.txt', 'w')
    save2 = open('output/valid.txt', 'w')
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
                print(pek)
            except:
                print W + '[ ' + G + 'VALID ' + W + '] ' + mail
                save2.write(mail + '\n')
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print W + '[ ' + R + 'INVALID ' + W + '] ' + mail
            else:
                print W + '[ ' + G + 'GATAU ' + W + '] ' + mail

    print 'Program finished'
    print 'Data saved valid.txt & invalid.txt'
    save.close()
    save2.close()

banner()
yahoolist()
