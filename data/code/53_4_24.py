def validate_side(side):
    if not isinstance(side, (int, float)):
        raise ValueError("Side must be a number")
    if side <= 0:
        raise ValueError("Side length must be positive")

def square_area(side):
    validate_side(side)
    return side * side

if __name__ == '__main__':
    sample_sides = [4.5, 6, 2.3, 8]
    for side in sample_sides:
        try:
            print(f"The area of the square with side {side} is: {square_area(side)}")
        except ValueError as e:
            print(e)