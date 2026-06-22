import math

def calculate_cylinder_surface_area(radius, height):
    lateral_area = 2 * math.pi * radius * height
    base_area = 2 * math.pi * radius * radius
    return lateral_area + base_area

if __name__ == '__main__':
    radius = 5
    height = 10
    result = calculate_cylinder_surface_area(radius, height)
    print(result)