import math

def calculate_cylinder_areas():
    radius = 5.0
    height = 10.0
    lateral_surface_area = 2 * math.pi * radius * height
    total_surface_area = 2 * math.pi * radius * (radius + height)
    return lateral_surface_area, total_surface_area

if __name__ == '__main__':
    lateral, total = calculate_cylinder_areas()
    print(lateral)
    print(total)