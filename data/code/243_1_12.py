import math

CIRCUMFERENCE_FACTOR = 2 * math.pi

def calculate_circumference(radius):
    return CIRCUMFERENCE_FACTOR * radius

if __name__ == '__main__':
    sample_radius = 5.0
    result = calculate_circumference(sample_radius)
    print(result)