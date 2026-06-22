import math

def compute_cylinder_surface_area():
    radius = 5
    height = 10
    base_area = math.pi * (radius ** 2)
    lateral_area = 2 * math.pi * radius * height
    total_area = 2 * base_area + lateral_area
    return total_area

if __name__ == '__main__':
    result = compute_cylinder_surface_area()
    print(result)