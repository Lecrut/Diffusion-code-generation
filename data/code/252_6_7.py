def validate_quantities(quantity1, quantity2):
    if not (isinstance(quantity1, (int, float)) and isinstance(quantity2, (int, float))):
        raise ValueError('Both quantities must be numbers')
    return True

def compare_two_simple_quantities_now_convert_all(quantity1, quantity2):
    validate_quantities(quantity1, quantity2)
    return quantity1 + quantity2
if __name__ == '__main__':
    result1 = compare_two_simple_quantities_now_convert_all(5, 3)
    print(result1)
    result2 = compare_two_simple_quantities_now_convert_all(10.5, 7.2)
    print(result2)