def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise TypeError("Side length must be a numeric value.")
    if side < 0:
        raise ValueError("Side length cannot be negative.")
    return side ** 2

if __name__ == '__main__':
    result = calculate_square_area(5)
    print(result)