def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise TypeError("Side length must be a numeric type.")
    if side < 0:
        raise ValueError("Side length must be non-negative.")
    return side * side

if __name__ == '__main__':
    result = calculate_square_area(5)
    print(result)