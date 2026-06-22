def validate_side_length(side):
    if not isinstance(side, (int, float)):
        raise ValueError("Side length must be a number")
    if side <= 0:
        raise ValueError("Side length must be positive")

def square_area(side):
    validate_side_length(side)
    return side * side

if __name__ == '__main__':
    sample_sides = [4.5, 2, 6, 9]
    for side in sample_sides:
        try:
            print(f"The area of the square with side {side} is: {square_area(side)}")
        except ValueError as e:
            print(e)