import math

def compute_cylinder_surface_areas(radius, height):
    lateral_area = 2 * math.pi * radius * height
    base_area = math.pi * radius * 2
    total_area = lateral_area + 2 * base_area
    return lateral_area, total_area

if __name__ == '__main__':
    r = 5.0
    h = 10.0
    lat, tot = compute_cylinder_surface_areas(r, h)
    print(lat)
    print(tot)