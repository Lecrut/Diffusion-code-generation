SIMPLE_QUANTITY_ONE = 10
SIMPLE_QUANTITY_TWO = 20

def compare_two_simple_quantities_now_calculate(quantity_one, quantity_two):
    if quantity_one > quantity_two:
        return 'First quantity is greater'
    elif quantity_one < quantity_two:
        return 'Second quantity is greater'
    else:
        return 'Quantities are equal'
if __name__ == '__main__':
    result = compare_two_simple_quantities_now_calculate(SIMPLE_QUANTITY_ONE, SIMPLE_QUANTITY_TWO)
    print(result)