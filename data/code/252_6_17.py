CONVERSION_FACTOR = 2.0
THRESHOLD = 10.0

def compare_two_simple_quantities_now_convert_all(quantity1, quantity2):
    converted_quantity1 = quantity1 * CONVERSION_FACTOR
    converted_quantity2 = quantity2 * CONVERSION_FACTOR
    if converted_quantity1 > THRESHOLD and converted_quantity2 > THRESHOLD:
        return (converted_quantity1, converted_quantity2)
    else:
        return (None, None)
if __name__ == '__main__':
    result1 = compare_two_simple_quantities_now_convert_all(5, 3)
    print(result1)
    result2 = compare_two_simple_quantities_now_convert_all(6, 4)
    print(result2)
    result3 = compare_two_simple_quantities_now_convert_all(7, 2)
    print(result3)