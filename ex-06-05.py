# Teo Espero
# BS Cloud and Systems Administration
# Western Governors University

# functions
def printGreetings():
    print('Exercise 06.05')
    print('This program locates numbers on a string.')
    print('------------------------------------------')

def getUserAction():
    global myString
    proceed = True
    while proceed:
        yourAnswer = input('Do you want to enter a custom string (y/n)? ').lower()

        if yourAnswer in 'yn':
            proceed = False
            if yourAnswer == 'y':
                myString = input('Enter a string: ').lower()
        else:
            print('Invalid response. y/n only.')
    return myString

def getNumber():
    number = ''
    dot = 0
    for piece in myString:
        if piece in '0123456789.':
            if piece == '.':
                dot = dot + 1
                if dot > 1:
                    piece = ''
            number = number + piece
    if '.' in number:
        return float(number)
    else:
        return int(number)

def showNumber(number):
    print('------------------------------------------')
    print(number, type(number))
    print('------------------------------------------')

# declarations
defString = 'X-DSPAM-Confidence: 0.8457   '
myString = defString

# begin

again = True
while again:
    printGreetings()
    myString = getUserAction()
    theNumber = getNumber()
    showNumber(theNumber)
    while True:
        tryAgain = input('Another run(y/n)? ').lower()
        if tryAgain in 'yn':
            break
        else:
            print('Invalid response. y/n only.')
    if tryAgain == 'n':
        again = False
    myString = defString

# end