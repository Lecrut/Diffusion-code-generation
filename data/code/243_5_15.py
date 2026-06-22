import math

CIRCUMFERENCE_CONSTANT = 2 * math.pi

def calculate_circle_circumference(radius):
    return CIRCUMFERENCE_CONSTANT * radius

if __name__ == '__main__':
    sample_radius = 2.5
    circumference = calculate_circle_circumference(sample_radius)
    print(circumference)