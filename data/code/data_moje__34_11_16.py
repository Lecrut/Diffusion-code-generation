import math

def compute_cylinder_surface_area(height, radius):
    lateral_area = 2 * math.pi * radius * height
    total_area = 2 * math.pi * radius * (height + radius)
    return lateral_area, total_area

if __name__ == '__main__':
    h = 10.0
    r = 5.0
    lat, tot = compute_cylinder_surface_area(h, r)
    print(lat)
    print(tot)