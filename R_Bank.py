MENU = f'''
============================
    Welcome!

    How may I help you?
    [a] Acess Account
    [c] Create Account
    [q] Quit
============================
'''
MENU_AFTER_ACCOUNT_ACCESSED = f''' 
============================
    Welcome back!

    How may I help you?
    [w] Withdraw
    [d] Deposit
    [e] Extract
    [q] Quit
============================
'''
users = [[f"user_0", "Gabriel", "Gabriel@email", "abcd", 1500.90, []]]
users_count = 1
account_accessed = False
account_acessed_user_info = ''
account_acessed_user_identification = ''

def acess_account():
    if users == []:
        print("There is no accounts registered!")

    else:
        user_name = input("Insert your Username: ")
        user_password = input("Insert your password: ")

        for user in users:
            if user_name == user[1] and user_password == user[3]:
                print(f"Welcome back, {user_name}!")
                global account_accessed
                account_accessed = True
                global account_acessed_user_info
                account_acessed_user_info = user_name
                global account_acessed_user_identification
                account_acessed_user_identification = user[0]

            else:
                print("Username or Password are incorrect or does not exist!")
                
def create_account():
    user_name = input("Insert your desired Username: ")
    user_email = input("Insert your email: ")
    extract = []
    global users_count

    if users == []:
        user_password = input("Insert your password: ")

        if len(user_password) >= 4 and len(user_password) <= 12:
            users_count += 1
            user = [f"user_{users_count}", user_name, user_email, user_password, 0.00, extract]
            users.append(user)
            print("Your account was created! Please access it in the Menu")

        else:
            print("Your password have less or more characters than allowed!/n")
    else:
        for user in users:
            if user_name == user[1] and user_email == user[2]:
                print("Este usuário já existe!")

            else:
                user_password = input("Insert your password: ")

                if len(user_password) >= 4 and len(user_password) <= 12:
                    users_count += 1
                    user = [f"user_{users_count}", user_name, user_email, user_password, 0.00, extract]
                    users.append(user)
                    print("Your account was created! Please access it in the Menu")
                    break

                else:
                    print("Your password have less or more characters than allowed!")

def withdraw_money(user_id):
    for user in users:
        if user_id == user[0]:
            withdraw = input("Please insert how much you want to withdraw: ")

            if int(withdraw) > user[4]:
                print("You cannot withdraw more money than you have in your account!")
            
            else:
                user[4] -= float(withdraw)
                print(f"Balance: ${user[4]:.2f}")
                user[5] += [f"Withdraw: ${withdraw}"]
        else:
            print("Sorry! Something went wrong.")

def deposit_money(user_id):
    for user in users:
        if user_id == user[0]:
            withdraw = input("Please insert how much you want to deposit: ")
            user[4] += float(withdraw)
            print(f"Balance: ${user[4]:.2f}")
            user[5] += [f"Deposit: ${withdraw}\n"]
        else:
            print("Sorry! Something went wrong.")

def extract_historic(user_id):
    for user in users:
        if user_id == user[0]:
            print(f'''
-----------------------------------------
            Your Extract
Actual Ballance: {user[4]:.2f}
-----------------------------------------
''')
            for operation in user[5]:
                print(operation)

while True:
    if account_accessed == True:
        account_acessed_user_info
        account_acessed_user_identification
        print(f'Account succesfully acessed, {account_acessed_user_info}!')
        print(MENU_AFTER_ACCOUNT_ACCESSED)
        activity = input("Choose the desired activity: ")

        if activity == 'w':
            withdraw_money(account_acessed_user_identification)
            continue

        elif activity == 'd':
            deposit_money(account_acessed_user_identification)
            continue

        elif activity == 'e':
            extract_historic(account_acessed_user_identification)
            continue

        elif activity == 'q':
            break

        else:
            print("The choosed option does NOT exist!.")

    else:    
        print(MENU)
        activity = input("Choose the desired activity: ")

        if activity == 'a':
            acess_account()
            continue

        elif activity == 'c':
            create_account()
            continue

        elif activity == 'q':
            break

        else:
            print("The choosed option does NOT exist!.")