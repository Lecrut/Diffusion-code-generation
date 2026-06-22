import math

def cylinder_surface_area():
    radius = 5
    height = 10
    lateral_area = 2 * math.pi * radius * height
    total_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
    return lateral_area, total_area

if __name__ == '__main__':
    result = cylinder_surface_area()
    print(result)