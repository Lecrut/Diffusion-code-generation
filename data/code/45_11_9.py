import math
PI = math.pi
RADIUS_VALUE = 3.0

def calculate_circle_area(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    area = calculate_circle_area(RADIUS_VALUE)
    print(area)