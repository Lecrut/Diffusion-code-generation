import math
RADIUS = 5

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return math.pi * radius ** 2
if __name__ == '__main__':
    try:
        area = calculate_circle_area(RADIUS)
        print(area)
    except ValueError as e:
        print(e)