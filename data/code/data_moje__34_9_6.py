import math

def calculate_cylinder_surface_area(radius, height):
    lateral_area = 2 * math.pi * radius * height
    base_area = 2 * math.pi * radius**2
    return lateral_area + base_area

if __name__ == '__main__':
    RADIUS = 5
    HEIGHT = 10
    surface_area = calculate_cylinder_surface_area(RADIUS, HEIGHT)
    print(surface_area)