import math

def cylinder_surface_area(radius, height):
    base_area = math.pi * (radius ** 2)
    lateral_area = 2 * math.pi * radius * height
    total_surface_area = 2 * base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    radius_value = 5
    height_value = 10
    result = cylinder_surface_area(radius_value, height_value)
    print(result)