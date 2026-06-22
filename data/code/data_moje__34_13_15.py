import math

def cylinder_surface_area(radius, height):
    base_area = math.pi * radius ** 2
    lateral_area = 2 * math.pi * radius * height
    return 2 * base_area + lateral_area

if __name__ == '__main__':
    sample_radius = 3.0
    sample_height = 5.0
    result = cylinder_surface_area(sample_radius, sample_height)
    print(result)