def calculate_square_area(side):
    if side <= 0:
        raise ValueError("Side length must be a positive number.")
    return side * side

if __name__ == '__main__':
    SIDES = [5, 10.5, -3, 0]
    for side in SIDES:
        try:
            area = calculate_square_area(side)
            print(f"The area of a square with side {side} is: {area}")
        except ValueError as e:
            print(f"Error for side {side}: {e}")