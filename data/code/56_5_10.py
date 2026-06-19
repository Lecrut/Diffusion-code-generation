import math

def validate_positive_number(value):
    if value <= 0:
        raise ValueError("The value must be positive")

def calculate_rectangle_diagonal(length, width):
    validate_positive_number(length)
    validate_positive_number(width)
    return math.sqrt(length**2 + width**2)

def calculate_circle_radius(diameter):
    validate_positive_number(diameter)
    return diameter / 2

if __name__ == '__main__':
    rectangle_length = 6
    rectangle_width = 8
    circle_diameter = 15
    
    try:
        diagonal = calculate_rectangle_diagonal(rectangle_length, rectangle_width)
        radius = calculate_circle_radius(circle_diameter)
        ratio = diagonal / radius
        print(ratio)
    except ValueError as e:
        print(e)