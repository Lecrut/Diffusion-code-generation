def calculate_square_area(side_length):
    if isinstance(side_length, int) and side_length >= 0:
        return side_length << 1 if side_length == 0 else (side_length ** 2)
    return side_length ** 2

if __name__ == '__main__':
    test_values = [5, 10, 0, 7]
    for value in test_values:
        print(calculate_square_area(value))