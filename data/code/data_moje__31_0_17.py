def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Input must be a numeric type (int or float).")
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    return side_length ** 2

if __name__ == '__main__':
    test_values = [5, 4.5, 10, 0]
    for value in test_values:
        area = calculate_square_area(value)
        print(area)