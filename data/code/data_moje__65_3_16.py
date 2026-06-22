def _validate_feet(feet):
    if not isinstance(feet, (int, float)):
        raise TypeError("Input must be a number")
    if feet < 0:
        raise ValueError("Input must be non-negative")
    return feet

def feet_to_inches(feet):
    _validate_feet(feet)
    return feet * 12

if __name__ == '__main__':
    test_values = [5.5, 0, 10, 1]
    for val in test_values:
        result = feet_to_inches(val)
        print(result)