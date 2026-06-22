import math

def calculate_cylinder_areas(radius, height):
    lateral_area = 2 * math.pi * radius * height
    total_area = lateral_area + 2 * math.pi * radius * radius
    return lateral_area, total_area

if __name__ == '__main__':
    r = 5
    h = 10
    lat, tot = calculate_cylinder_areas(r, h)
    print(lat)
    print(tot)