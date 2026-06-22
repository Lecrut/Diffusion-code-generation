SIMPLE_QUANTITY_1 = 15
SIMPLE_QUANTITY_2 = 20

COMPARISON_DICT = {
    'greater': 'is greater',
    'less': 'is less',
    'equal': 'are equal'
}

def compare_two_simple_quantities_now_calculate(quantity1, quantity2):
    if quantity1 > quantity2:
        return f'Quantity 1 {COMPARISON_DICT["greater"]}'
    elif quantity1 < quantity2:
        return f'Quantity 2 {COMPARISON_DICT["less"]}'
    else:
        return f'Quantities {COMPARISON_DICT["equal"]}'

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_calculate(SIMPLE_QUANTITY_1, SIMPLE_QUANTITY_2)
    print(result)