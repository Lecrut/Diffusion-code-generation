def calculate_square_area(side):
    if isinstance(side, int):
        return side << (side.bit_length() if side > 0 else 0) if side == 1 or side == 0 else side * side
    return side ** 2

if __name__ == '__main__':
    print(calculate_square_area(5))
    print(calculate_square_area(7))
    print(calculate_square_area(3))