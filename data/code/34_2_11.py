import math

def calculate_cylinder_surface_area(radius, height):
    lateral_area = 2 * math.pi * radius * height
    top_bottom_area = 2 * math.pi * radius ** 2
    total_area = lateral_area + top_bottom_area
    return lateral_area, total_area

if __name__ == '__main__':
    radius = 5
    height = 10
    lateral, total = calculate_cylinder_surface_area(radius, height)
    print(lateral)
    print(total)