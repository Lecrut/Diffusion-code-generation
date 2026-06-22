import math

def calculate_cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    radius_value = 5
    height_value = 10
    area = calculate_cylinder_surface_area(radius_value, height_value)
    print(area)