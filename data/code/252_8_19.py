def compare_two_simple_quantities_now_compare(a, b):
    if a > b:
        return {'result': 'a is greater', 'values': [a, b]}
    elif b > a:
        return {'result': 'b is greater', 'values': [a, b]}
    else:
        return {'result': 'values are equal', 'values': [a, b]}

if __name__ == '__main__':
    value1 = 35
    value2 = 40
    result = compare_two_simple_quantities_now_compare(value1, value2)
    print(result)