import math

def compute_shape_properties(radius, side_length):
    circle_circumference = 2 * math.pi * radius
    square_perimeter = 4 * side_length
    return (circle_circumference, square_perimeter)

if __name__ == '__main__':
    sample_circle_radius = 3.5
    sample_square_side_length = 6.0
    result = compute_shape_properties(sample_circle_radius, sample_square_side_length)
    print(result)