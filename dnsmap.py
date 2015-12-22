'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

#!/bin/python



# Colours
##D  = "\033[0m";  
##W  = "\033[01;37m";  
##O  = "\033[01;33m"; 
##SUCESS = "\033[01;32m";
##FAIL = "\033[01;31m";

import socket
import sys
import os
os.system("clear")
print ("+----------------------------------------------------------------------------+")
print ("|                                      DNSMap                                |")
print ("+----------------------------------------------------------------------------+")
print ("|                            by Ronel Llarenas.                       |")
print ("|                         $ Wget >                     |")
print ("+----------------------------------------------------------------------------+")
print ("")
###########
domain = input("Set domain: ") # www.domain.com
 
try:
    ip = socket.gethostbyname( domain )
###########
except socket.gaierror:
    print ('Invalid Domain.\n\n\n\n\n\n\n')
    sys.exit()
print ("+-------------------------+")
print ("| DNS   : " +ip+ "     |")
print ("+-------------------------+")

       
