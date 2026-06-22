def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise TypeError("Side length must be a numeric value (int or float).")
    if side < 0:
        raise ValueError("Side length cannot be negative.")
    return side * side

if __name__ == '__main__':
    test_side = 5
    area = calculate_square_area(test_side)
    print(area)