def _validate_side(length):
    if not isinstance(length, int):
        raise TypeError("Side length must be an integer")
    if length < 0:
        raise ValueError("Side length must be non-negative")
    return True

def calculate_square_area(side):
    _validate_side(side)
    return side * side

if __name__ == '__main__':
    HARMONIC_SIDE = 42
    area = calculate_square_area(HARMONIC_SIDE)
    print(area)