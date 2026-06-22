import math

def calculate_cylinder_surface_area(radius, height):
    base_area = math.pi * radius * radius
    side_area = 2 * math.pi * radius * height
    total_surface_area = 2 * base_area + side_area
    return total_surface_area

if __name__ == '__main__':
    radius = 3.0
    height = 5.0
    area = calculate_cylinder_surface_area(radius, height)
    print(area)