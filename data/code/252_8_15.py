def compare_two_simple_quantities_now_compare():
    VALUE_1 = 42
    VALUE_2 = 24
    
    if VALUE_1 > VALUE_2:
        return {'result': 'VALUE_1 is greater', 'values': [VALUE_1, VALUE_2]}
    elif VALUE_1 < VALUE_2:
        return {'result': 'VALUE_2 is greater', 'values': [VALUE_1, VALUE_2]}
    else:
        return {'result': 'values are equal', 'values': [VALUE_1, VALUE_2]}

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_compare()
    print(result)