import math

def calculate_cylinder_areas(radius, height):
    lateral_surface_area = 2 * math.pi * radius * height
    total_surface_area = 2 * math.pi * radius * (radius + height)
    return lateral_surface_area, total_surface_area

if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    lateral, total = calculate_cylinder_areas(radius, height)
    print(lateral)
    print(total)