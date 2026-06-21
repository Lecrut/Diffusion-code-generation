def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise TypeError("Side length must be a numeric value")
    if side < 0:
        raise ValueError("Side length must be non-negative")
    return side ** 2

if __name__ == '__main__':
    print(calculate_square_area(5))
    print(calculate_square_area(0))
    print(calculate_square_area(3.5))