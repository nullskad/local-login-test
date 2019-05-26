import os 
import random 
import time 
import getpass 

def change_password(username):
    os.system('cls')
    path = "Data/users/"+username+"/password"
    pwchange = open(path, "w")
    new_pw = getpass.getpass("New password: ")
    while new_pw.__len__ < 2:
        print("Password too weak, try again")
        if new_pw.__len__ > 2:
            break
    
    pwchange.write(new_pw)
    print("Password has been changed!")
    user_panel(username)



def user_panel(user):
    os.system("cls")
    print("Logged in as",user)
    print("Type help for list of all commands")
    print("out = Log out from current account")
    print('chp = Change password')
    usr = input("Console: ") 
    if usr == "out":
        os.system('cls')
        print("Logged out from",user)
        main()
    if usr == "chp":
        change_password(user)

def login(usrname, pswd):
    try:
        path = "Data/users/"+usrname+"/"

        login_manager = open(path+'password', "r")
        for line in login_manager:
            if pswd == line:
                print('Logging in as',usrname)
                time.sleep(2)
                user_panel(usrname)
            else:
                print("Wrong password")
                main()

    except:
        print('User doesn\'t exist')
        main()
def registration():
    try:
        username = input("Username: ")
        usrc = len(username)
        if usrc < 2:
            os.system('cls')
            print("Username too short")
            registration()
        if usrc > 8:
            os.system('cls')
            print("Username can't be over 8 characters")
            registration()
        print("##########################################################")
        print("For security reasons password wont be shown, just type it.")
        password = getpass.getpass()
        passlen = len(password)
        while passlen < 2:
            print("Password must be at least 3 characters long")
            password = getpass.getpass()
            passlen = len(password)
            if passlen > 2:
                break
        passconfirm = getpass.getpass("Confirm password: ")
        while passconfirm != password:
            os.system('cls')
            print("Passwords don't match")
            passconfirm = getpass.getpass("Confirm password: ")
            if passconfirm == password:
                print("Password has been setup.")
                break
        path = "Data/users/"+username+"/"
        os.makedirs(path)
        prs = open(path+'password', "w")
        prs.write(password)
        prs.close()
        prs = open(path+'info.txt', "w+")
        prs.write("Username: " + username)
        prs.write("\nPassword: " + password)
        prs.close()
        print("User " + username + " has been created, you can login now.")
        main()

    except:
        os.system('cls')
        print("User already exists")
        registration()

def main():
    print("##############")
    print("q = Exit")
    print("reg = Register")
    print("login = Login")
    print("##############")
    wait = input("Choice: ")
    if wait == "q":
        print("Exiting in 1 second")
        time.sleep(1)
        exit()
    if wait == "reg":
        os.system('cls')
        registration()
    if wait == "login":
        username = input("Username: ")
        password = getpass.getpass()
        login(username, password)
    else:
        os.system("cls")
        print("Invalid choice")
        main()

main()


