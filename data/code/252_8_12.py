def compare_two_simple_quantities_now_compare(value1, value2):
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        raise ValueError("Both values must be numbers")
    
    if value1 > value2:
        return {'result': 'value1 is greater', 'values': [value1, value2]}
    elif value1 < value2:
        return {'result': 'value2 is greater', 'values': [value1, value2]}
    else:
        return {'result': 'values are equal', 'values': [value1, value2]}

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_compare(42, 24)
    print(result)