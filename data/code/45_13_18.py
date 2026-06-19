import math
PI = math.pi
RADIUS = 5.0

def compute_circle_area(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    area = compute_circle_area(RADIUS)
    print(area)