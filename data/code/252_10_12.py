SIMPLE_QUANTITY_1 = 10
SIMPLE_QUANTITY_2 = 20

def compare_two_simple_quantities_now_calculate(quantity1, quantity2):
    if quantity1 > quantity2:
        return f'{quantity1} is greater than {quantity2}'
    elif quantity1 < quantity2:
        return f'{quantity1} is less than {quantity2}'
    else:
        return f'{quantity1} is equal to {quantity2}'
if __name__ == '__main__':
    result = compare_two_simple_quantities_now_calculate(SIMPLE_QUANTITY_1, SIMPLE_QUANTITY_2)
    print(result)