import math

def cylinder_surface_area(radius, height):
    base_area = math.pi * radius ** 2
    lateral_area = 2 * math.pi * radius * height
    return 2 * base_area + lateral_area
if __name__ == '__main__':
    radius = 5
    height = 10
    surface_area = cylinder_surface_area(radius, height)
    print(surface_area)