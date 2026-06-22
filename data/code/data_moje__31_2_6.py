def square_area(side):
    if isinstance(side, int) and side >= 0:
        return side << side.bit_length() - 1 if side > 0 else 0
    return side ** 2

if __name__ == '__main__':
    result = square_area(5)
    print(result)