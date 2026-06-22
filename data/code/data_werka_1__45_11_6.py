import math

CIRCLE_CONFIG = {
    'radius': 6.0,
    'unit': 'cm'
}

def compute_area_of_circle(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    radius_value = CIRCLE_CONFIG['radius']
    area = compute_area_of_circle(radius_value)
    print(f"The area of the circle with radius {radius_value} {CIRCLE_CONFIG['unit']} is {area:.2f} square {CIRCLE_CONFIG['unit']}.")