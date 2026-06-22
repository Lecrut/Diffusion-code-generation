import math
CIRCLE_PROPERTIES = {'pi': math.pi, 'diameter_factor': 2}

def compute_circle_perimeter(radius):
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    diameter = CIRCLE_PROPERTIES['diameter_factor'] * radius
    return CIRCLE_PROPERTIES['pi'] * diameter
if __name__ == '__main__':
    sample_radius = 10.0
    perimeter = compute_circle_perimeter(sample_radius)
    print(perimeter)