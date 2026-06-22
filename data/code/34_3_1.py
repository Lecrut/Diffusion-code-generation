import math

def calculate_cylinder_surface_area(radius, height):
    lateral_area = 2 * math.pi * radius * height
    base_area = math.pi * radius ** 2
    total_area = lateral_area + 2 * base_area
    return total_area

if __name__ == '__main__':
    r = 5
    h = 10
    result = calculate_cylinder_surface_area(r, h)
    print(result)