import math

def validate_radius(radius):
    if radius <= 0:
        raise ValueError("Radius must be positive")

def validate_side_length(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be positive")

def calculate_circumference_and_perimeter(radius, side_length):
    validate_radius(radius)
    validate_side_length(side_length)
    
    circle_circumference = 2 * math.pi * radius
    square_perimeter = 4 * side_length
    return (circle_circumference, square_perimeter)

if __name__ == '__main__':
    sample_circle_radius = 6.0
    sample_square_side_length = 8.0
    
    try:
        result = calculate_circumference_and_perimeter(sample_circle_radius, sample_square_side_length)
        print(result)
    except ValueError as e:
        print(e)