import math
CIRCLE_RADIUS = 5

def compute_circle_area(radius):
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return math.pi * radius ** 2
if __name__ == '__main__':
    try:
        area = compute_circle_area(CIRCLE_RADIUS)
        print(area)
    except ValueError as e:
        print(e)