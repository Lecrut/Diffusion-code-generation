import math

PI_VALUE = math.pi
ONE_THIRD = 1.0 / 3.0

def compute_cone_volume(radius, height):
    base_area = PI_VALUE * (radius * radius)
    volume = ONE_THIRD * base_area * height
    return volume

if __name__ == '__main__':
    r = 7.0
    h = 12.0
    result = compute_cone_volume(r, h)
    print(result)