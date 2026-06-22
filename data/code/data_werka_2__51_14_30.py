import math
CIRCLE_CONSTANTS = {'pi': math.pi}

def compute_circle_perimeter(radius):
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return 2 * CIRCLE_CONSTANTS['pi'] * radius
if __name__ == '__main__':
    sample_radius = 10.0
    perimeter = compute_circle_perimeter(sample_radius)
    print(perimeter)