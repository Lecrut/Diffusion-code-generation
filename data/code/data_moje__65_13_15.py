UNIT_CONVERSION_FACTOR = 12

def validate_numeric_input(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a numeric type (int or float)")
    return True

def convert_feet_to_inches(feet_value):
    validate_numeric_input(feet_value)
    return feet_value * UNIT_CONVERSION_FACTOR

if __name__ == '__main__':
    test_cases = [10, 0.5, 7.25, -3.5]
    for val in test_cases:
        result = convert_feet_to_inches(val)
        print(result)