def square_area(side):
    if side < 0:
        return 0
    if isinstance(side, int):
        return side << side.bit_length() - 1 if side > 0 else 0
    return side ** 2

if __name__ == '__main__':
    result = square_area(4)
    print(result)