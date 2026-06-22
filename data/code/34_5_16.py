import math

def calculate_cylinder_surface_area(radius, height):
    base_area = math.pi * radius ** 2
    lateral_area = 2 * math.pi * radius * height
    return 2 * base_area + lateral_area

if __name__ == '__main__':
    r = 5.0
    h = 10.0
    surface_area = calculate_cylinder_surface_area(r, h)
    print(surface_area)