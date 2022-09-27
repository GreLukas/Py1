#1
x =  int(input("Number Expected "))
y = 101 - x 
print(y)

#2
n = int(input("cislo "))
sum = 0
for num in range(1, n + 1, 1):
    sum = sum + num
print("soucet je: ", sum)

#3
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")

#4
list = [12,75,150,180,145,525]
for i in list:
    if 150 < i:
        continue
    elif i > 500:
        break 
    elif((i%5==0)):
        print(i)