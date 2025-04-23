# -----------------------------------------------------------
# Program: pizza.py
# Author: Lavender Moraa
# Due: 04/06/2024
# Class time 9:30am - 10:45 am
# Project: Falcon Fries
# Description: Calculating the cost of an order
# at Falcon Pizza Shop. Customers get discounts and coupon
# codes depending on how much they buy
# -----------------------------------------------------------

#  Constants
PIZZA_PRICE_REGULAR = 7.50
PIZZA_PRICE_DISCOUNT = 5.00
PIZZA_DISCOUNT = 4

FRIES_PRICE = 0.75
FRIES_FREE = 2
FRIES_FREE_COUNT = 2

DRINK_PRICE = 1.75

DISCOUNT_10 = 0.10
DISCOUNT_20 = 0.20
#DISCOUNT_NONE = 0.0


def main():    #Input
    num_pizzas = int(input("Enter number of pizzas: "))
    num_fries = int(input("Enter number of fries: "))
    num_drinks = int(input("Enter number of soft drinks: "))
    coupon_code = int(input("Enter coupon code (0, 1, or 2): "))

    #GetPizzaCost
    if num_pizzas >= PIZZA_DISCOUNT:
        pizza_cost = num_pizzas * PIZZA_PRICE_DISCOUNT
    else:
        pizza_cost = num_pizzas * PIZZA_PRICE_REGULAR

    #GetFriesCost
    if num_pizzas >= FRIES_FREE:
        fries_to_pay = max(0, num_fries - FRIES_FREE_COUNT)
    else:
        fries_to_pay = num_fries
    fries_cost = fries_to_pay * FRIES_PRICE

    #GetDrinkCost
    drink_cost = num_drinks * DRINK_PRICE

    #Calculate subtotal
    subtotal = pizza_cost + fries_cost + drink_cost

    #GetDiscount
    if coupon_code == 1:
        discount = subtotal * DISCOUNT_10
    elif coupon_code == 2:
        discount = subtotal * DISCOUNT_20
    else:
        discount = 0.0

    #Calculate amount due
    amount_due = subtotal - discount

    #Output
    print("\n----- Falcon Pizza Receipt -----")
    print(f"Pizza cost:        ${pizza_cost:.2f}")
    print(f"Fries cost:        ${fries_cost:.2f}")
    print(f"Soft drink cost:   ${drink_cost:.2f}")
    print(f"Subtotal:          ${subtotal:.2f}")
    print(f"Discount:          -${discount:.2f}")
    print(f"Amount Due:        ${amount_due:.2f}")


main()
input('this statement is used by the TA grading, \nmeant to pause the program, just enter Y')