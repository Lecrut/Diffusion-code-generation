def square_area(side):
    if isinstance(side, int) and side >= 0:
        return side << (side.bit_length()) if side == 0 else side * side
    return side * side

if __name__ == '__main__':
    print(square_area(5))
    print(square_area(10))
    print(square_area(0))
    print(square_area(7.5))