import math
RADIUS = 5

def calculate_circle_area(radius):
    return math.pi * radius ** 2
if __name__ == '__main__':
    area = calculate_circle_area(RADIUS)
    print(area)