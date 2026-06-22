def calculate_square_area(side_length):
    if isinstance(side_length, int):
        return side_length << side_length.bit_length() - (side_length.bit_length() > 0) if side_length > 0 else 0
    return side_length * side_length

if __name__ == '__main__':
    print(calculate_square_area(5))
    print(calculate_square_area(10))
    print(calculate_square_area(3.5))