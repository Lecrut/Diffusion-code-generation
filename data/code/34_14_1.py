import math

def compute_cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    radius = 5
    height = 10
    print(compute_cylinder_surface_area(radius, height))