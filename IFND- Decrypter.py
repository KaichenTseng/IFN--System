Ncopyright=('''Copyright (c) 2001-2020 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.''')
Ncredits=(''' Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.''')
Nlicense=('''A. HISTORY OF THE SOFTWARE
==========================

Python was created in the early 1990s by Guido van Rossum at Stichting
Mathematisch Centrum (CWI, see http://www.cwi.nl) in the Netherlands
as a successor of a language called ABC.  Guido remains Python's
principal author, although it includes many contributions from others.

In 1995, Guido continued his work on Python at the Corporation for
National Research Initiatives (CNRI, see http://www.cnri.reston.va.us)
in Reston, Virginia where he released several versions of the
software.

In May 2000, Guido and the Python core development team moved to
BeOpen.com to form the BeOpen PythonLabs team.  In October of the same
year, the PythonLabs team moved to Digital Creations, which became
Zope Corporation.  In 2001, the Python Software Foundation (PSF, see
https://www.python.org/psf/) was formed, a non-profit organization
created specifically to own Python-related Intellectual Property.
Zope Corporation was a sponsoring member of the PSF.

All Python releases are Open Source (see http://www.opensource.org for
the Open Source Definition).  Historically, most, but not all, Python
Hit Return for more, or q (and Return) to quit: ''')
from time import sleep
import sys
import time
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./3000)

print('''



   IFND-(解密系統)D 版本1.2 is Starting...
   -------------------------------



''') ; sleep(2)
print('''
   Warning: Please use Python 3.10 or above for full encryption/decryption services.

''') ; sleep(3)
print('''    Loading Tasklist...
    ----------------------
    ''') ; sleep(2)

print('''    Volume in IFND-HD is IFND_DISK
     Directory of IFND-HD:\
''') ; sleep(1.5)
print('''


    IO       SYS*   223148   7-11-95   9:50a
''') ; sleep(1)
slowprint('''    IFND  SYS*        4   7-11-95   9:50a
    COMMAND  COM     92870   7-11-95   9:50a
    AUTOEXEC BAT        25   7-11-95   9:50a
    CONFIG   SYS        40   7-11-95   9:50a
    COUNTRY  SYS     27094   7-11-95   9:50a
    DISPLAY  SYS     17175   7-11-95   9:50a
    EGA      CPI     58870   7-11-95   9:50a
    EGA2     CPI     58870   7-11-95   9:50a
    EGA3     CPI     48973   7-11-95   9:50a
    FDISK    EXE     59128   7-11-95   9:50a
    FORMAT   COM     40135   7-11-95   9:50a
    HIMEM    SYS     32935   7-11-95   9:50a
    KEYB     COM     19927   7-11-95   9:50a
    KEYBOARD SYS     34566   7-11-95   9:50a
    KEYBRD2  SYS     31942   7-11-95   9:50a
    MODE     COM     29191   7-11-95   9:50a
    OEMSETUP BIN      3270   7-11-95   9:50a
    OEMSETUP EXE     78668   7-11-95   9:50a
           19 file(s)     856831 bytes

                      595968 bytes free''') ; sleep(1.5)
print('''
    --------------------------------------------------
''')
slowprint('''    MINI     CAB    441905   7-11-95   9:50a
    PRECOPY1 CAB    484352   7-11-95   9:50a
    WB16OFF  EXE       537   7-11-95   9:50a
    SCANDISK EXE    134738   7-11-95   9:50a
    DOSSETUP BIN     72246   7-11-95   9:50a
    WINSETUP BIN    159504   7-11-95   9:50a
    DELTEMP  COM       496   7-11-95   9:50a
    SAVE32   COM       920   7-11-95   9:50a
    EXTRACT  EXE     46656   7-11-95   9:50a
    SCANPROG EXE      4438   7-11-95   9:50a
    SETUP    EXE      5184   7-11-95   9:50a
    SMARTDRV EXE     45145   7-11-95   9:50a
    XMSMMGR  EXE     14144   7-11-95   9:50a
    SCANDISK PIF       995   7-11-95   9:50a
    README   TXT      7302   7-11-95   9:50a
    SETUP    TXT     34612   7-11-95   9:50a
           16 file(s)    1453174 bytes

                               0 bytes free


                           ''') ; sleep(3)

print('''       Exiting Tasklist Check...
      --------------------------''') ; sleep(2)


print('''    Volume in drive IFN-HD is DISK13
     Directory of A:\

    IFND_13 CAB    981813   7-11-95   9:50a
            1 file(s)     981813 bytes
                      733184 bytes READY...

''')
print('''       Startup Complete... Loading System...
    --------------------------------------------''') ; sleep(4)
print('''

    IFN 1.0.2 (v1.0.2:6503f05dd5) 
    [Tlang 3.0 (tlang-800.0.59)] on darwin
    Type "help", "Ncopyright", "Ncredits" or "Nlicense" for more information.

''')

#Encrypter 
from time import sleep

enter_encrypted_text = input('''      Enter message to be decrypted : ''')
print(''' 
    ''')

decrypted_text = ""

for char in enter_encrypted_text:
    
    com_char = ord(char)
    
    com_char = (com_char) - 1
    
    reverser = chr(com_char)
    
    decrypted_text = decrypted_text + str(reverser)
    
print('''
      your decrypted message is : ''',decrypted_text)
print('''



                WARNING: This message would be deleted within 60 seconds''')

sleep(60) #this window won't close for 5 seconds, enough to see the greeting 