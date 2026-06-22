def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise TypeError("Side length must be a numeric type.")
    if side < 0:
        raise ValueError("Side length must be non-negative.")
    return side * side

if __name__ == '__main__':
    sample_side = 5.0
    result = calculate_square_area(sample_side)
    print(result)
    sample_side_2 = 10
    result_2 = calculate_square_area(sample_side_2)
    print(result_2)