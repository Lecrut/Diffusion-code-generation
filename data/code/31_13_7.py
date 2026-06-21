def _validate_side(side):
    if not isinstance(side, (int, float)):
        raise TypeError("Side length must be a number")
    if side < 0:
        raise ValueError("Side length must be non-negative")
    return True

def calculate_square_area(side_length):
    _validate_side(side_length)
    return side_length ** 2

if __name__ == '__main__':
    side = 20
    area = calculate_square_area(side)
    print(area)