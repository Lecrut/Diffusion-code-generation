def validate_side_length(side):
    if not isinstance(side, (int, float)):
        raise TypeError("Side length must be a number")
    if side <= 0:
        raise ValueError("Side length must be positive")

def calculate_square_area(side):
    validate_side_length(side)
    return side * side

if __name__ == '__main__':
    sample_sides = [4.5, 6, 2.3]
    for side in sample_sides:
        try:
            area = calculate_square_area(side)
            print(f"The area of the square with side {side} is: {area}")
        except (TypeError, ValueError) as e:
            print(e)