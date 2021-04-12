import random
from user import User

def main():
    
    while True:
        print("welcome to password locker!!")
        print('\n')
        print("select a short code to navigate through:to create new user use 'nu':To log in to your account 'lg' or 'ex' to exit:
        short_code input().lower()
        print('\n')
        
        if short_code == 'nu':
           print('create username')
           created_user_name = input()
           
           print('create password')
           created_user_password = input()
           
           print('confirm passowrd')
           confirm_password = input()
           
           while confirm_password != created_user_password:
               print('invalid password')
               print('enter your password')
               created_user_password = input()
               print('confrim your password')
               confirm_password = input()
           else:
               print("congratulations {created_user_name} ! you've succesfully created your account")
               print('\n')
               print("proceed to login")
               print("Username")
               entered_username = input()
               print("your password")
               entered_password = input()
               
            while entered_username != created_user_name or entered_password != created_user_password:
               print("Invalid username or password")
               print("Username")
               entered_username = input()
               print("Your password")
               entered_password = input()
            else:
               print("welcome: {enterd_username} to your account")
               print('\n')
       
        elif short_code == 'lg':
           print("Welcome")
           print("Enter user name")
           default_user_name = input()
           
           
           print("Enter password")
           default_user_password = input()
           print('\n')
           while default_user_name != 'testuser' or default_user_password != '09876':
               print ("Wrong userName or password. Username 'testuser' and password '09876'")
               print("Enter user name")
               default_user_name =input()
                
               print("Enter password")
               default_user_password = input()
               print("\n")
           else:
                print("Login Success")
                print("\n")
                print("\n")
        
        elif short_code == 'ex':
            break
        else:
            print("Enter valid code to continue")
 
if _name_== '_main_':
    main()                    
               
           
                 