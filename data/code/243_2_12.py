import math

CIRCLE_PERIMETER_FACTOR = 2 * math.pi

def calculate_circle_perimeter(radius):
    return CIRCLE_PERIMETER_FACTOR * radius

if __name__ == '__main__':
    sample_radius = 5.0
    print(calculate_circle_perimeter(sample_radius))