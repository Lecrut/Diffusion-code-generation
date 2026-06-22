SIMPLE_QUANTITY_1 = 10
SIMPLE_QUANTITY_2 = 20

def compare_two_simple_quantities_now_calculate(q1, q2):
    if q1 > q2:
        return 'q1 is greater'
    elif q1 < q2:
        return 'q2 is greater'
    else:
        return 'q1 and q2 are equal'
if __name__ == '__main__':
    result = compare_two_simple_quantities_now_calculate(SIMPLE_QUANTITY_1, SIMPLE_QUANTITY_2)
    print(result)