import math
CIRCLE_CONSTANTS = {'pi': math.pi}

def calculate_circle_perimeter(radius):
    return 2 * CIRCLE_CONSTANTS['pi'] * radius
if __name__ == '__main__':
    hard_coded_radius = 10.0
    perimeter = calculate_circle_perimeter(hard_coded_radius)
    print(perimeter)