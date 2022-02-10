import random

#user input of the length of the password
password_length = int(input('enter the length of the password, must be more than 8 and less than 17:  '))

while password_length > 8 or password_length < 17 :
    #characters used
    passowrd_characters='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()'
    #password randomizer
    random_password = ''.join(random.sample(passowrd_characters,password_length))
    #if the password is too short or too long will ask to put in a new number
    if password_length <= 8 or password_length >= 17:
        print('Password needs to be at least 9 characters long but no more than 17')
        password_length = int(input('Enter a password witht the correct length:  '))
    #will print out a password when after an acceptable lenght has been put in
    elif password_length > 8 or password_length < 17:
        print('Your Password: ' + random_password)
        break
    

#todo print password to file
#file = open('C:\\Ran.txt' , 'x')
#file = open('C:\\Ran.txt' , 'w')
#file.write("Added to file: " + random_password)
#file.close()
