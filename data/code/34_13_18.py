import math

def _base_area(radius):
    return math.pi * radius * radius

def _lateral_area(radius, height):
    return 2 * math.pi * radius * height

def cylinder_surface_area(radius, height):
    if radius < 0 or height < 0:
        return 0.0
    b = _base_area(radius)
    l = _lateral_area(radius, height)
    return 2 * b + l

if __name__ == '__main__':
    r = 5.0
    h = 10.0
    print(cylinder_surface_area(r, h))