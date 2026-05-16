def calculate_square_area(side):
    if side <= 0:
        raise ValueError("Side length must be positive.")
    return side * side
if __name__ == '__main__':
    test_side_positive = 5
    test_side_zero = 0
    test_side_negative = -3
    try:
        area1 = calculate_square_area(test_side_positive)
        print(f"The area of a square with side {test_side_positive} is: {area1}")
        area2 = calculate_square_area(10.5)
        print(f"The area of a square with side 10.5 is: {area2}")
        calculate_square_area(test_side_zero)
    except ValueError as e:
        print(f"Error caught for side {test_side_zero}: {e}")
    try:
        calculate_square_area(test_side_negative)
    except ValueError as e:
        print(f"Error caught for side {test_side_negative}: {e}")