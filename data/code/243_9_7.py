import math

def calculate_circle_circumference(radius):
    CIRCUMFERENCE_FACTOR = 2 * math.pi
    return CIRCUMFERENCE_FACTOR * radius

if __name__ == '__main__':
    sample_radius = 3.14
    circumference = calculate_circle_circumference(sample_radius)
    print(circumference)