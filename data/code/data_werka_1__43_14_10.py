def calculate_square_area(side):
    if side <= 0:
        raise ValueError("Side length must be a positive number.")
    return side * side

if __name__ == '__main__':
    test_sides = [7, 12.3, -5, 0]
    for side in test_sides:
        try:
            area = calculate_square_area(side)
            print(f"The area of a square with side {side} is: {area}")
        except ValueError as e:
            print(f"Error for side {side}: {e}")