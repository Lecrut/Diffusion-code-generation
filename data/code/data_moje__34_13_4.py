import math

def _compute_base_area(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius ** 2

def _compute_lateral_area(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    return 2 * math.pi * radius * height

def cylinder_surface_area(radius, height):
    base_area = _compute_base_area(radius)
    lateral_area = _compute_lateral_area(radius, height)
    return 2 * base_area + lateral_area

if __name__ == '__main__':
    r = 3.5
    h = 7.0
    print(cylinder_surface_area(r, h))