import math

def _base_area(radius):
    return math.pi * radius ** 2

def calculate_cone_volume(radius, height):
    if radius < 0 or height < 0:
        return 0.0
    area = _base_area(radius)
    return area * height / 3.0

if __name__ == '__main__':
    r = 10
    h = 20
    v = calculate_cone_volume(r, h)
    print(v)