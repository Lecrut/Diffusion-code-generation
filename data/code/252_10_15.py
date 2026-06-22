SIMPLE_QUANTITY_1 = 10
SIMPLE_QUANTITY_2 = 20

def compare_two_simple_quantities_now_calculate(q1, q2):
    if q1 > q2:
        return f'{q1} is greater than {q2}'
    elif q1 < q2:
        return f'{q1} is less than {q2}'
    else:
        return f'{q1} is equal to {q2}'
if __name__ == '__main__':
    result = compare_two_simple_quantities_now_calculate(SIMPLE_QUANTITY_1, SIMPLE_QUANTITY_2)
    print(result)