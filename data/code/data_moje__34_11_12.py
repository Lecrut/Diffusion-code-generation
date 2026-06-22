import math

PI = math.pi

def cylinder_areas(r, h):
    if r < 0 or h < 0:
        raise ValueError
    lat = 2 * PI * r * h
    total = lat + 2 * PI * r * r
    return lat, total

if __name__ == '__main__':
    radius = 7.5
    height = 12.0
    l, t = cylinder_areas(radius, height)
    print(l)
    print(t)