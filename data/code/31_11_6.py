def _validate_side(side):
    if not isinstance(side, (int, float)):
        raise TypeError("Side must be a number")
    if side < 0:
        raise ValueError("Side must be non-negative")
    return side

def compute_square_area(side):
    _validate_side(side)
    return side ** 2

if __name__ == '__main__':
    side_length = 15
    area = compute_square_area(side_length)
    print(area)