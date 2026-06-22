SIMPLE_QUANTITY_1 = 10
SIMPLE_QUANTITY_2 = 20

def is_valid_quantity(quantity):
    if not isinstance(quantity, (int, float)):
        raise ValueError("Quantity must be a number")

def compare_two_simple_quantities_now_calculate(quantity1, quantity2):
    is_valid_quantity(quantity1)
    is_valid_quantity(quantity2)
    
    if quantity1 > quantity2:
        return 'Quantity 1 is greater'
    elif quantity1 < quantity2:
        return 'Quantity 2 is greater'
    else:
        return 'Quantities are equal'

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_calculate(SIMPLE_QUANTITY_1, SIMPLE_QUANTITY_2)
    print(result)