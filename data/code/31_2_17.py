def calculate_square_area(side_length):
    if isinstance(side_length, int) and side_length >= 0:
        return side_length << side_length.bit_length() - 1 if side_length == 0 else (side_length * side_length)
    return side_length ** 2

if __name__ == '__main__':
    print(calculate_square_area(4))
    print(calculate_square_area(5))
    print(calculate_square_area(0))
    print(calculate_square_area(2.5))