# Importing menus to program
from menu import *

# Blank customer menu to store values and calculate total cost
customer_menu = []

# Chaos method; Nested While Loops 💀💀


def menu_prompt(menu):
    # Drink Loop; Only one Drink per PERSON (I hate my program users)
    while True:
        for drinks in menu['drinks']:
            # Woahhh we're using f strings and calling indices of nested dictionaries
            print(f'{drinks}: ${format(menu['drinks'][drinks], '.2f')}')
        # Inputs are set to all lower; Makes it easier for me to process user input :3
        drink_choice = input('Choose a drink ').lower()
        if drink_choice in menu['drinks'].keys():
            # f string
            print(f'You have chosen {drink_choice}')
            customer_menu.append(menu['drinks'][drink_choice])
            break
        else:
            print('invalid input!')
            continue
    # Same thing but it's appetizers :P
    while True:
        for apps in menu['apps']:
            print(f'{apps}: ${format(menu['apps'][apps], '.2f')}')
        apps_choice = input('Choose an appetizer/side ').lower()
        if apps_choice in menu['apps'].keys():
            print(f'You have chosen {apps_choice}')
            customer_menu.append(menu['apps'][apps_choice])
            break
        else:
            print('invalid input')
            continue
    # Blah blah blah same thing
    while True:
        for entrees in menu['entrees']:
            print(f'{entrees}: ${format(menu['entrees'][entrees], '.2f')}')
        entrees_choice = input('Choose an entree ').lower()
        if entrees_choice in menu['entrees'].keys():
            print(f'You have chosen {entrees_choice}')
            customer_menu.append(menu['entrees'][entrees_choice])
            break
        else:
            print('invalid input')
            continue
    choice = input('Do you want dessert? ').lower()
    if choice == 'yes':
        while True:
            for desserts in menu['desserts']:
                print(f'{desserts}: ${format(menu['desserts'][desserts], '.2f')}')
            desserts_choice = input('Choose a dessert? ').lower()
            if desserts_choice in menu['desserts'].keys():
                print(f'You have chose {desserts_choice}')
                break
            else:
                print('invalid input')
                continue
        menu_calc(customer_menu)
    elif choice == 'no':
        menu_calc(customer_menu)


def menu_calc(meh):
    total = 0
    for i in meh:
        total += i
    # Tax is an arbitrary value that I made up :D
    tax = total % 2
    total += tax
    print(f'Your total will be ${format(total, '.2f')}')


print('Welcome to the (insert restaurant name) restaurant!')
while True:
    menu = input('What menu would you like to view? Breakfast, Lunch, or Dinner? ').lower()
    if menu == 'breakfast':
        menu_prompt(breakfast_menu)
    elif menu == 'lunch':
        menu_prompt(lunch_menu)
    elif menu == 'dinner':
        menu_prompt(dinner_menu)
    else:
        print('invalid input')
        continue
    break
