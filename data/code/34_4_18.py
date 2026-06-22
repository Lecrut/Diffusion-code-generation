import math

def compute_cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    r = 3
    h = 5
    result = compute_cylinder_surface_area(r, h)
    print(result)