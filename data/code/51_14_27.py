import math

def calculate_circle_perimeter(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    diameter = 2 * radius
    return math.pi * diameter

if __name__ == '__main__':
    sample_radius = 10.0
    perimeter = calculate_circle_perimeter(sample_radius)
    print(perimeter)