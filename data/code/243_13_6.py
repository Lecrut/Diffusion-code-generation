import math

CIRCLE_PERIMETER_FACTOR = 2 * math.pi

def calculate_circle_perimeter(radius):
    return CIRCLE_PERIMETER_FACTOR * radius

if __name__ == '__main__':
    sample_radius = 10.5
    perimeter = calculate_circle_perimeter(sample_radius)
    print(perimeter)