import re

b=[]

#code to validate email
e='[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'  #email logic code

email=input('Enter the email:')
file1=open("myfile.txt","r")
L=file1.readlines()
def check(email):
 for i in L:
    L1=i.split()
    if email in L1:
        print("Already your email has been registered")
        print("Login with your password")
        break

 else:
        if re.search(e,email):
                return b.append(email)
        else:
                print("Please enter a valid mail")
check(email) 

#code to validate password
password=input('Enter the password:')
flag=0
if not re.search('[a-z]',password):
            flag=1
if not re.search('[0-9]',password):
            flag=1
if not re.search('[A-Z]',password):
            flag=1
if not re.search('[!@#$%&]',password):
            flag=1
if len(password)<5 or len(password)>16:
            flag=1
        
if (flag==0):
            b.append(password)
else:
            print("Strong Password is suggested")
            print("A strong password should contain one Uppercase, one Lowercase, one Digit and a Symbol.")
            print("Run the code again !!")



#condition for registering in a file
if len(b)==2:
    print("Registered in a file")
    file1 = open("myfile.txt", "a") 
    for i in b:
        file1.write(i)
        file1.write("\n")
    file1= open("myfile.txt","r")
    print(file1.read())
    file1.close()
else:
    pass