_FOOT_TO_INCH_FACTOR = 12

def _is_valid_number(value):
    if not isinstance(value, (int, float)):
        return False
    return True

def feet_to_inches(feet):
    if not _is_valid_number(feet):
        raise TypeError("Input must be a number")
    if feet < 0:
        raise ValueError("Feet cannot be negative")
    return feet * _FOOT_TO_INCH_FACTOR

if __name__ == '__main__':
    test_cases = [3.0, 7.25, 12.0]
    for case in test_cases:
        print(feet_to_inches(case))