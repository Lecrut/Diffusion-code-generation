import math

PERIMETER_MULTIPLIER = 2 * math.pi

def calculate_circle_perimeter(radius):
    return PERIMETER_MULTIPLIER * radius

if __name__ == '__main__':
    sample_radius = 5.0
    perimeter = calculate_circle_perimeter(sample_radius)
    print(perimeter)