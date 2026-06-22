import math

def calculate_cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    r = 5
    h = 10
    area = calculate_cylinder_surface_area(r, h)
    print(area)