SIMPLE_QUANTITY_1 = 25
SIMPLE_QUANTITY_2 = 15

def compare_two_simple_quantities_now_calculate(quantity1, quantity2):
    if not isinstance(quantity1, (int, float)) or not isinstance(quantity2, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return 'Quantity 1 is greater' if quantity1 > quantity2 else 'Quantity 2 is greater' if quantity1 < quantity2 else 'Quantities are equal'

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_calculate(SIMPLE_QUANTITY_1, SIMPLE_QUANTITY_2)
    print(result)