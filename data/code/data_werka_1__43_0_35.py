def validate_side_length(side):
    if not isinstance(side, (int, float)):
        raise ValueError("Side length must be a number.")
    if side <= 0:
        raise ValueError("Side length must be positive.")

def calculate_square_area(side):
    validate_side_length(side)
    return side * side

if __name__ == '__main__':
    sample_sides = [3, 5, 10]
    for side in sample_sides:
        area = calculate_square_area(side)
        print(f"The area of a square with side length {side} is {area}.")