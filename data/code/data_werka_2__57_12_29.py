import math
CIRCLE_RADIUS = 5

def compute_circle_area(radius):
    return math.pi * radius ** 2
if __name__ == '__main__':
    area_result = compute_circle_area(CIRCLE_RADIUS)
    print(f'The area of the circle with radius {CIRCLE_RADIUS} is: {area_result}')