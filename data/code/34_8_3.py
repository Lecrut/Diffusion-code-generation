import math

def calculate_cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    r = 10.5
    h = 30.25
    result = calculate_cylinder_surface_area(r, h)
    print(result)