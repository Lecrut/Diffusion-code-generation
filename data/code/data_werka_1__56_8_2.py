import math

SHAPE_CONSTANTS = {
    'circle': {'pi': math.pi},
    'square': {'multiplier': 4}
}

def calculate_circumference_and_perimeter(radius, side_length):
    circle_circumference = 2 * SHAPE_CONSTANTS['circle']['pi'] * radius
    square_perimeter = SHAPE_CONSTANTS['square']['multiplier'] * side_length
    return (circle_circumference, square_perimeter)

if __name__ == '__main__':
    sample_radius = 7.5
    sample_side_length = 3.2
    result = calculate_circumference_and_perimeter(sample_radius, sample_side_length)
    print(result)