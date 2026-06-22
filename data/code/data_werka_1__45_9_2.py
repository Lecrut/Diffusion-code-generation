import math
CIRCLE_CONSTANTS = {'pi': math.pi}

def calculate_circle_area(radius):
    return CIRCLE_CONSTANTS['pi'] * radius ** 2
if __name__ == '__main__':
    sample_radius = 7.5
    area = calculate_circle_area(sample_radius)
    print(area)