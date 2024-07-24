import random

print("Wecome to the Py_password Generator!")
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=[1,2,3,4,5,6,7,8,9]
symbols=["@","$","!","&","*","#"]

nl_want=int(input("How many letters would you like in your password?\n"))
ns_want=int(input("How many symbols would you like\n"))
nn_want=int(input("How many numbers would you like?\n"))
empty_=[]

for i in range(0,nl_want):
    n=random.randint(0,len(letters)-1)
    let=letters[n]
    empty_.append(str(let))

for i in range(0,ns_want):
    n=random.randint(0,len(symbols)-1)
    sym=symbols[n]
    empty_.append(str(sym))

for i in range(0,nn_want):
    n=random.randint(0,len(numbers)-1)
    num=numbers[n]
    empty_.append(str(num))

password=""
for i in range(0,len(empty_)):
    n=random.randint(0,len(empty_)-1)
    unknown=empty_[n]
    password+=unknown

print(f"Here is your password: {password}")