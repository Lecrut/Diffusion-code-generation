MAX_VALUE = 100

def compare_two_simple_quantities_now_compare():
    value1 = 42
    value2 = 24
    if value1 > MAX_VALUE or value2 > MAX_VALUE:
        return {'error': 'One of the values exceeds the maximum allowed'}
    if value1 > value2:
        return {'result': 'value1 is greater', 'values': [value1, value2]}
    elif value1 < value2:
        return {'result': 'value2 is greater', 'values': [value1, value2]}
    else:
        return {'result': 'values are equal', 'values': [value1, value2]}

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_compare()
    print(result)