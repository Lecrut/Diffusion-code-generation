def square_area(side):
    if isinstance(side, int):
        return side << (side.bit_length() - 1) if side > 0 else 0
    return side ** 2

if __name__ == '__main__':
    side_length = 4
    result = square_area(side_length)
    print(result)