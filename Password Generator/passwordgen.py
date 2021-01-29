#imports
import random
import string

#globals
validPasswordCharacters = ""
colors = {'BOLD': '\033[1m', 'END': '\033[0m'}

#def: generateValidPasswordString
def generateValidPasswordString(lowercaseFlag, uppercaseFlag, numberFlag, specialCharFlag):
    global validPasswordCharacters
    if(lowercaseFlag):
        validPasswordCharacters += string.ascii_lowercase
    if(uppercaseFlag):
        validPasswordCharacters += string.ascii_uppercase
    if(numberFlag):
        validPasswordCharacters += string.digits
    if(specialCharFlag):
        validPasswordCharacters += string.punctuation

#def: printGeneratedPassword
def printGeneratedPassword(generatedPassword):
    print('Password generated! Here is the result:\n' + colors['BOLD'] + generatedPassword + colors['END'])
    promptForRerun()

#def: promptForRerun
def promptForRerun():
    runAgain = input('Generate another password? [y/n]: ')
    if runAgain == 'y':
        main()
    else:
        print('Thank you for using the password generator! Goodbye.')

#def: generatePassword
def generatePassword(length):
    global validPasswordCharacters
    generatedPassword = ''.join(random.choice(validPasswordCharacters) for _ in range(length))
    printGeneratedPassword(generatedPassword)

#def: getPasswordLength
def getPasswordLength():
    while True:
        try:
            passwordLength = int(input("Enter password length: "))
            break
        except ValueError:
            print("That's not a number!")
    return passwordLength

#def: getLowercaseInput
def getLowercaseInput():
    while True:
        lowercaseFlag = input("Are lowercase letters okay? [y/n]:")
        if lowercaseFlag == 'y':
            lowercaseFlag = True
            break
        elif lowercaseFlag == 'n':
            lowercaseFlag = False
            break
        else:
            print("Invalid y/n response. Try again!")
    
    return lowercaseFlag

#def: getUppercaseInput
def getUppercaseInput():
    while True:
        uppercaseFlag = input("Are uppercase letters okay? [y/n]:")
        if uppercaseFlag == 'y':
            uppercaseFlag = True
            break
        elif uppercaseFlag == 'n':
            uppercaseFlag = False
            break
        else:
            print("Invalid y/n response. Try again!")

    return uppercaseFlag

#def: getNumbersInput
def getNumbersInput():
    while True:
        numberFlag = input("Are numbers okay? [y/n]:")
        if numberFlag == 'y':
            numberFlag = True
            break
        elif numberFlag == 'n':
            numberFlag = False  
            break
        else:
            print("Invalid y/n response. Try again!")

    return numberFlag

#def: getSpecialCharInput
def getSpecialCharInput():
    while True:
        specialCharFlag = input("Are special characters okay? [y/n]:")
        if specialCharFlag == 'y':
            specialCharFlag = True
            break
        elif specialCharFlag == 'n':
            specialCharFlag = False
            break
        else:
            print("Invalid y/n response. Try again!")

    return specialCharFlag

#def: main
def main():
    passwordLength = getPasswordLength()
    lowercaseFlag = getLowercaseInput()
    uppercaseFlag = getUppercaseInput()
    numberFlag = getNumbersInput()
    specialCharFlag = getSpecialCharInput()
    
    if (lowercaseFlag or uppercaseFlag or numberFlag or specialCharFlag):
        generateValidPasswordString(lowercaseFlag, uppercaseFlag, numberFlag, specialCharFlag)
    else:
        print("No valid combination of characters can be made from selected input. Please try again!")
        main()

    generatePassword(passwordLength)

main()