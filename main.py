from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine_1 = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True
menu = Menu()


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to have??: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine_1.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine_1.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



