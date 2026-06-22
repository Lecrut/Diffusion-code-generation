CONVERSION_FACTOR = 12

def _validate_feet_value(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a number")
    if value < 0:
        raise ValueError("Feet value cannot be negative")
    return value

def feet_to_inches(feet):
    valid_feet = _validate_feet_value(feet)
    return valid_feet * CONVERSION_FACTOR

if __name__ == '__main__':
    test_cases = [10, 3.75, 0, 100.0]
    for val in test_cases:
        print(feet_to_inches(val))