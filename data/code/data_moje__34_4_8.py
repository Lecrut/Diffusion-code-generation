import math

def surface_area_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    r = 5
    h = 10
    result = surface_area_cylinder(r, h)
    print(result)