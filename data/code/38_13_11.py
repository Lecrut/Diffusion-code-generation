import math

THIRD = 1 / 3
PI = math.pi

def calculate_cone_volume(radius, height):
    base_area = PI * radius ** 2
    return base_area * height * THIRD

if __name__ == '__main__':
    r = 6.0
    h = 15.0
    print(calculate_cone_volume(r, h))