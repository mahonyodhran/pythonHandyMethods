def ask_user(question):
    check = str(input(question + " [Y/N]: ")).lower().strip()
    try:
        if check[:1] == 'y':
            return True
        elif check[:1] == 'n':
            return False
        else:
            print('Invalid Input')
            return ask_user(question)
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return ask_user()

answer = ask_user('Enter question here: ')
print(answer)