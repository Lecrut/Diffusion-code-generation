import math

CIRCLE_PERIMETER_TO_RADIUS_RATIO = 2 * math.pi

def calculate_perimeter(radius):
    return CIRCLE_PERIMETER_TO_RADIUS_RATIO * radius

if __name__ == '__main__':
    sample_radius = 10.0
    perimeter = calculate_perimeter(sample_radius)
    print(f"Radius: {sample_radius}")
    print(f"Perimeter: {perimeter}")