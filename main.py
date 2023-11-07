def tables(num):
    for i in range (11):
        print(f"{num} X {i} = {num * i}")

def repeat(num):
    for i in range (num):
        print(f"This number made me repeat for {num} times")

print("1. Tables \n2. Repeat")
option = int(input("option >> "))
num = int(input("Enter number >> "))

if option==1:
    tables(num)
elif option==2:
    repeat(num)
else:
    print("Option invalid . Try again")
