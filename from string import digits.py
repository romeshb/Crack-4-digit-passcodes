#from cs502021p Cybersecurity (pre-release)

from string import digits 
from itertools import product 

for passcode in product(digits, repeat = 4):
    print(*passcode)