import math

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    print(cylinder_surface_area(3.0, 5.0))