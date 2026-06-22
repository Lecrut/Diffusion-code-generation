import math
RADIUS = 6.0

def compute_circle_area(radius):
    return math.pi * radius ** 2
if __name__ == '__main__':
    area = compute_circle_area(RADIUS)
    print(area)