def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise TypeError("Side length must be a numeric type.")
    if side < 0:
        raise ValueError("Side length cannot be negative.")
    return side ** 2

if __name__ == '__main__':
    side_length = 5
    area = calculate_square_area(side_length)
    print(area)