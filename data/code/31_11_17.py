def _validate_positive_number(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Side length must be a number")
    if value <= 0:
        raise ValueError("Side length must be positive")
    return True

def compute_square_area(side):
    _validate_positive_number(side)
    return side * side

if __name__ == '__main__':
    test_value = 15
    result = compute_square_area(test_value)
    print(result)