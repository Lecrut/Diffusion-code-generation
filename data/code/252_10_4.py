SIMPLE_QUANTITY_1 = 15
SIMPLE_QUANTITY_2 = 30

def compare_two_simple_quantities_now_calculate(quantity1, quantity2):
    if quantity1 > quantity2:
        return 'Quantity 1 is greater'
    elif quantity1 < quantity2:
        return 'Quantity 2 is greater'
    else:
        return 'Quantities are equal'

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_calculate(SIMPLE_QUANTITY_1, SIMPLE_QUANTITY_2)
    print(result)