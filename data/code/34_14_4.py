import math

def compute_cylinder_surface_area():
    radius = 5.0
    height = 10.0
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

if __name__ == '__main__':
    result = compute_cylinder_surface_area()
    print(result)