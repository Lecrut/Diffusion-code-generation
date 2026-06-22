import math

def compute_cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    r = 5
    h = 10
    area = compute_cylinder_surface_area(r, h)
    print(area)