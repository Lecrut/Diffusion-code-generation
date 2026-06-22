import math

def cylinder_surface_area(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return 2 * math.pi * radius * height + 2 * math.pi * radius ** 2

if __name__ == '__main__':
    r = 3.0
    h = 5.0
    area = cylinder_surface_area(r, h)
    print(area)