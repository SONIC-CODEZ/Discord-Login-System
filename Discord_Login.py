import random
import time


class Discord:
    def __init__(self, username, password, age, email):
        self.username = username
        self.password = password
        self.age = age
        self.email = email

    def checkAge(self):
        if int(self.age) < 13:
            exit("Underage!")

    def checkEmail(self):
        if '@gmail.com' not in self.email or '@ymail.com' not in self.email:
            exit("Invalid email!")

        elif '@gmail.com' in self.email or '@ymail.com' in self.email:
            print('Updated!')

    def checkPassword(self):
        if int(self.password) > 100:
            pass

    def formatUsername(self):
        return f'The formatted username is {self.username}#{random.randint(1000, 10000)}'


if __name__ == '__main__':
    while True:
        # USERNAME
        input_for_username = input('Enter a username: ')
        arukovic = Discord(input_for_username, 143, '467', 'abc@gmail.com')
        arukovic.username = input_for_username
        print('Generating your formatted username...')
        time.sleep(2)
        print(arukovic.formatUsername())
        # PASSWORD
        time.sleep(1)
        input_for_password = input('Enter your password: ')
        arukovic.password = input_for_password
        arukovic.checkPassword()
        # AGE
        time.sleep(1)
        input_for_age = input('Enter your age: ')
        arukovic.age = input_for_age
        arukovic.checkAge()
        # EMAIL
        time.sleep(1)
        input_for_email = input('Enter your email: ')
        arukovic.email = input_for_email
        # TODO: FIX EMAIL
        # arukovic.checkEmail()
        # SHOW RESULTS
        print(f'Generating results @{arukovic.username}')
        time.sleep(2)
        print(f"Your username: {arukovic.username}, Your password: {arukovic.password}, Your age: {arukovic.age}, "
              f"Your email is: {arukovic.email}")
        break
