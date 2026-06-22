import math

def calculate_cylinder_surface_area(radius, height):
    base_area = math.pi * radius ** 2
    lateral_area = 2 * math.pi * radius * height
    total_area = 2 * base_area + lateral_area
    return total_area

if __name__ == '__main__':
    radius_value = 5.0
    height_value = 10.0
    result = calculate_cylinder_surface_area(radius_value, height_value)
    print(result)