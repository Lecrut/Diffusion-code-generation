import math

def compute_cylinder_surface_area(radius, height):
    lateral_area = 2 * math.pi * radius * height
    total_area = lateral_area + 2 * math.pi * (radius ** 2)
    return lateral_area, total_area

if __name__ == '__main__':
    r = 3
    h = 5
    lateral, total = compute_cylinder_surface_area(r, h)
    print(lateral)
    print(total)