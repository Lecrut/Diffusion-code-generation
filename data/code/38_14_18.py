import math

CONE_FACTOR = math.pi / 3

def calculate_cone_volume(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive")
    base_area = math.pi * radius * radius
    return base_area * height * (1.0 / 3.0)

if __name__ == '__main__':
    r = 3.0
    h = 4.0
    vol = calculate_cone_volume(r, h)
    print(vol)