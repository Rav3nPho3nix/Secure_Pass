# Made by Rav3nPho3nix
# https://github.com/Rav3nPho3nix/

# Here, I use only base64 to encrypt and decrypt values
# But you can change the encrpytion and decryption functions
# by your own method

import json,os,base64

# encryption // YOU CAN CHANGE HERE
def encrypt(x):
    x = base64.b64encode(str(x).encode("utf-8"))
    return x

# decryption // YOU CAN CHANGE HERE
def decrypt(x):
    x = (str(base64.b64decode((x)[2:-1])))[2:-1]
    return x

# delete data
def delete(data,names,values,numbers):

    os.system("cls")
    print("You have:")
    for i in range(len(names)):
        x = decrypt(names[i])
        print(f"{i+1}. {x}")

    z = input("What password to delete ? ")

    try:z=int(z)
    except:main()

    for i in range(numbers):
        if z==i+1:
            del names[z-1]
            del values[z-1]

    with open(f"{os.getcwd()}\pass_data.json", "w") as file:
        json.dump(data, file)

    print(f"Password n°{z} deleted !")
    input()
    main()

# display data
def display(data,names,values,numbers):

    os.system("cls")
    print("You have:")

    for i in range(len(names)):
        x=decrypt(names[i])
        print(f"{i+1}. {x}")

    x=input("> ")
    try:x=int(x)
    except:main()

    for i in range(numbers):
        if x==i+1:
            os.system("cls")
            x=decrypt(values[i])
            print(x)
            input()
            main()

# add data
def add_values(data):

    os.system("cls")
    print("Add data :")

    name = encrypt(input("Title : "))
    value = encrypt(input("Your password : "))


    data["name"].append(str(name))
    data["value"].append(str(value))
    with open(f"{os.getcwd()}\pass_data.json", "w") as file:
        json.dump(data, file)

    input()
    main()

# console
def main():

    with open(f"{os.getcwd()}\pass_data.json", "r") as file:
        data = json.load(file)
    os.system("cls")
    inp = input("Do you want to :\n1. See your passwords\n2. Add data\n3. Delete data\nPress 'q' to quit\n> ")
    
    names = data["name"]
    values = data["value"]
    numbers = len(names)

    if inp=="1": display(data,names,values,numbers)
    elif inp=="2":add_values(data)
    elif inp=="3":delete(data,names,values,numbers)
    elif inp=="q":exit()
    else: main()

main()