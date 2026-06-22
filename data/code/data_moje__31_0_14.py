def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise TypeError("Side length must be a number")
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side ** 2

if __name__ == '__main__':
    print(calculate_square_area(5))