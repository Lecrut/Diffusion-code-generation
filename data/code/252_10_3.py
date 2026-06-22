SIMPLE_QUANTITY_1 = 10
SIMPLE_QUANTITY_2 = 20

def compare_two_simple_quantities_now_calculate(quantity1, quantity2):
    if not isinstance(quantity1, (int, float)) or not isinstance(quantity2, (int, float)):
        raise ValueError("Both inputs must be numbers")
    if quantity1 > quantity2:
        return 'Quantity 1 is greater'
    elif quantity1 < quantity2:
        return 'Quantity 2 is greater'
    else:
        return 'Quantities are equal'

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_calculate(SIMPLE_QUANTITY_1, SIMPLE_QUANTITY_2)
    print(result)