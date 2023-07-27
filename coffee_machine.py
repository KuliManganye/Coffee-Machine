MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):   
    """Returns True when order can be made, and False when resources are insufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
    return is_enough


    
def process_coins():
    """returns the total calculated from coins inserted."""
    amount_paid = 0
    quarters = 0.25
    dimes = 0.1
    nickles = 0.05
    pennies = 0.01

    print("Please insert coins.")
    quarters_inputed = int(input("How many quarters?: "))
    dimes_inputed = int(input("How many dimes?: ")) 
    nickles_inputed = int(input("How many nickles: "))
    pennies_inputed = int(input("How many pennies?: "))

    amount_paid = quarters_inputed * quarters
    amount_paid += dimes_inputed * dimes
    amount_paid += nickles_inputed * nickles
    amount_paid += pennies_inputed * pennies
    return amount_paid



def is_transaction_successful(money_received, drink_cost):
    """"Returns True when the paymens is accepted or False if money is insufficent"""
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = money_received - drink_cost
        print(f"Here is ${change:.2f} in change")
        return True
    else:
        print("Sorry that is not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ ")
    


        
coffee_machine_on = True

while coffee_machine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == "off":
        coffee_machine_on = False
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])
