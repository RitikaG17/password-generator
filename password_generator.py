import random

def passwordGenerator():
    lowerchars=['a','b','c','d','e']
    upperchars=['A','B','C','D','E']
    specialchars=['&','!','*']
    numericchars=['1','2','3','4','5']
   
    all_chars = lowerchars + upperchars + specialchars + numericchars
  
    password = ''.join(random.choice(all_chars) for _ in range(16))
    return password

print(passwordGenerator())