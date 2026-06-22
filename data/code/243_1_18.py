import math

CIRCLE_RADIUS = 5.0

def calculate_circumference(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = CIRCLE_RADIUS
    circumference = calculate_circumference(sample_radius)
    print(circumference)