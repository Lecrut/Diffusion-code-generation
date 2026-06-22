import math

def cylinder_areas():
    radius = 3
    height = 5
    lateral_surface_area = 2 * math.pi * radius * height
    total_surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
    return lateral_surface_area, total_surface_area

if __name__ == '__main__':
    lat, tot = cylinder_areas()
    print(lat)
    print(tot)