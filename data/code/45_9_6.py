import math

CIRCLE_CONSTANTS = {'pi': 3.141592653589793}

def calculate_circle_area(radius):
    return CIRCLE_CONSTANTS['pi'] * radius ** 2

if __name__ == '__main__':
    sample_radius = 10.0
    area = calculate_circle_area(sample_radius)
    print(area)