import math

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    r = 5.0
    h = 10.0
    result = cylinder_surface_area(r, h)
    print(result)