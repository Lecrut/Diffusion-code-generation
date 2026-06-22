import math
PI = math.pi
RADIUS = 3.0

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError('Radius must be a number.')
    if radius < 0:
        raise ValueError('Radius cannot be negative.')

def calculate_circle_area(radius):
    validate_radius(radius)
    return PI * radius ** 2
if __name__ == '__main__':
    try:
        area = calculate_circle_area(RADIUS)
        print(area)
    except Exception as e:
        print(e)