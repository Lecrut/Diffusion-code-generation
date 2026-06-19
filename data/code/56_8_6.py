import math

CIRCLE_CIRCUMFERENCE_FACTOR = 2 * math.pi
SQUARE_PERIMETER_FACTOR = 4

def calculate_shapes(radius, side_length):
    circle_circumference = CIRCLE_CIRCUMFERENCE_FACTOR * radius
    square_perimeter = SQUARE_PERIMETER_FACTOR * side_length
    return (circle_circumference, square_perimeter)

if __name__ == '__main__':
    sample_radius = 3.0
    sample_side_length = 6.0
    result = calculate_shapes(sample_radius, sample_side_length)
    print(result)