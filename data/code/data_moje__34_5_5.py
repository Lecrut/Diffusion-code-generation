import math

def calculate_cylinder_surface_area(radius, height):
    lateral_area = 2 * math.pi * radius * height
    base_area = 2 * math.pi * (radius ** 2)
    total_area = lateral_area + base_area
    return total_area

if __name__ == '__main__':
    radius = 3.0
    height = 5.0
    result = calculate_cylinder_surface_area(radius, height)
    print(result)