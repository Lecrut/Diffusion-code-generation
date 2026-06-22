import math

def cylinder_surface_area(radius, height):
    if radius <= 0 or height <= 0:
        return 0.0
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    r = 3.0
    h = 5.0
    result = cylinder_surface_area(r, h)
    print(result)