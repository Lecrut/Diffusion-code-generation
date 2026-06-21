import math

CIRCLE_CONFIG = {"name": "circle", "constant_key": "pi"}

def get_circle_area(radius):
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    radius = 10
    config = CIRCLE_CONFIG
    area = get_circle_area(radius)
    print(area)