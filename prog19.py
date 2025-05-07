username = input("Enter Username :")
password = input("Enter Password :")

correct_username = 'admin'
correct_password = '1234'

if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("CANNOT ENTER ! WRONG INFORMATION")