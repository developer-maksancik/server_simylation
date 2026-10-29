import random
import time 

server = 0
max_server = 45
elso = False
cist = 0
users = 0

def sety():
    global cist
    if users == 7:
        cist = 1
    elif users == 15:
        cist = 2
    elif users == 24:
        cist = 3
    elif users == 33:
        cist = 4
    elif users == 44:
        cist = 5
    elif users == 47:
        print("КРИТИЧЕСКАЯ НАГРУЗКА")
        bknd = 0
        for i in range(100):
            clr()
            print(f"перезагрузка сервера: {i}%")
            time.sleep(0.2)
            bknd = bknd + 1
        cist = 0
        
        
def usr():
    global users
    if cist == 0: 
        users = random.randint(1, 7)
    elif cist == 1:
        users = random.randint(8, 15)
    elif cist == 2:
        users = random.randint(16, 24)
    elif cist == 3:
        users = random.randint(25, 33)
    elif cist == 4:
        users = random.randint(34, 44)
    elif cist == 5:
        users = random.randint(45, 47)

def clr():
    for i in range(40):
        print()
        
def seto():
    global elso
    usr()
    if users > 45:
        elso = True
    load = users / max_server
    Fload = load * 100
    print(" SERVER API 23_US ")
    print("correct login / maks_12 / kz_us")
    print(f"на сервере {users} человек")
    print(f"сервер загужен на {Fload:.1f}%")
    if elso == True:
        print("критическая нагрузка!")
        elso = False
    print()
    time.sleep(5)
    clr()
    
    
    
while True:
    sety()
    seto()

    

