import math
RADIUS = 15.0

def compute_circle_area(radius):
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return math.pi * radius ** 2
if __name__ == '__main__':
    try:
        area = compute_circle_area(RADIUS)
        print(f'The area of the circle with radius {RADIUS} is {area:.2f}')
    except ValueError as e:
        print(e)