SAMPLE_VALUE_1 = 42
SAMPLE_VALUE_2 = 24

def compare_two_simple_quantities_now_compare(value1, value2):
    if value1 > value2:
        return {'result': 'value1 is greater', 'values': [value1, value2]}
    elif value1 < value2:
        return {'result': 'value2 is greater', 'values': [value1, value2]}
    else:
        return {'result': 'values are equal', 'values': [value1, value2]}
if __name__ == '__main__':
    result = compare_two_simple_quantities_now_compare(SAMPLE_VALUE_1, SAMPLE_VALUE_2)
    print(result)