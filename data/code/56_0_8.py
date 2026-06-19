import math

def validate_radius(radius):
    if radius <= 0:
        raise ValueError("Radius must be positive")

def validate_side(side):
    if side <= 0:
        raise ValueError("Side length must be positive")

def calculate_circle_area(radius):
    validate_radius(radius)
    return math.pi * radius ** 2

def calculate_circle_perimeter(radius):
    validate_radius(radius)
    return 2 * math.pi * radius

def calculate_square_area(side):
    validate_side(side)
    return side ** 2

def calculate_square_perimeter(side):
    validate_side(side)
    return 4 * side

if __name__ == '__main__':
    circle_radius = 7.0
    square_side_length = 6.0
    try:
        circle_area = calculate_circle_area(circle_radius)
        circle_perimeter = calculate_circle_perimeter(circle_radius)
        square_area = calculate_square_area(square_side_length)
        square_perimeter = calculate_square_perimeter(square_side_length)
        print(f"Circle Area: {circle_area}")
        print(f"Circle Perimeter (Circumference): {circle_perimeter}")
        print(f"Square Area: {square_area}")
        print(f"Square Perimeter: {square_perimeter}")
    except ValueError as e:
        print(e)