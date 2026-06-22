import math
PI = math.pi

def calculate_area(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    RADIUS = 8.0
    area = calculate_area(RADIUS)
    print(area)