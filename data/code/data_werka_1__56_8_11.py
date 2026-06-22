import math

def calculate_circle_circumference(radius):
    return 2 * math.pi * radius

def calculate_square_perimeter(side_length):
    return 4 * side_length

def calculate_shapes(radius, side_length):
    circle_circumference = calculate_circle_circumference(radius)
    square_perimeter = calculate_square_perimeter(side_length)
    return (circle_circumference, square_perimeter)

if __name__ == '__main__':
    sample_radius = 3.5
    sample_side_length = 6.0
    result = calculate_shapes(sample_radius, sample_side_length)
    print(result)