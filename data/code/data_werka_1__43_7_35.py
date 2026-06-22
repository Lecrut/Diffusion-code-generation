def calculate_square_area(side: float) -> float:
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side ** 2

if __name__ == '__main__':
    test_values = [3.0, 5.0, 7.0]
    for value in test_values:
        area = calculate_square_area(value)
        print(f"The area of the square with side {value} is {area}")