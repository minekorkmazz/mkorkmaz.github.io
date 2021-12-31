for i in range(5,0,-1):
    for j in range(i):
        print("* ", end="")
    
    if (i != 1):
        print("")
        

for i in range(6):
    for j in range(i):
        print("* ", end="")
    print("")

sayac = 0
for i in range(2000, 3001):
    if(i % 5 == 0 and i % 7 != 0):
        sayac += 1

print(sayac)