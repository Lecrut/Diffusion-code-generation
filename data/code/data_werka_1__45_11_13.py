import math
CIRCLE_RADIUS = 3.0

def compute_circle_area(radius):
    return math.pi * radius ** 2
if __name__ == '__main__':
    area_result = compute_circle_area(CIRCLE_RADIUS)
    print(area_result)