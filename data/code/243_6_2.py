import math

circle_properties = {
    'radius': 100,
    'perimeter_formula': lambda r: 2 * math.pi * r
}

def calculate_circle_perimeter():
    radius = circle_properties['radius']
    perimeter = circle_properties['perimeter_formula'](radius)
    return float(perimeter)

if __name__ == '__main__':
    print(calculate_circle_perimeter())