import math
CIRCLE_RADIUS = 5

def calculate_circle_area(radius):
    return math.pi * radius ** 2
if __name__ == '__main__':
    circle_area = calculate_circle_area(CIRCLE_RADIUS)
    print(circle_area)