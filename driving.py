country = input('Where are you from? ')
age = input('How old are you? ')
age = int(age)

if country == 'taiwan':
    if age >= 18:
        print('You can take the drivers license')
    else:
        print('You cannot take the drivers license yet')
