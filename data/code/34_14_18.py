import math

def calculate_cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)
if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    surface_area = calculate_cylinder_surface_area(radius, height)
    print(surface_area)