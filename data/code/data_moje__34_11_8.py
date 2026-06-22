import math

def calculate_cylinder_surface_areas(radius, height):
    lateral_area = 2 * math.pi * radius * height
    total_area = 2 * math.pi * radius * (radius + height)
    return lateral_area, total_area

if __name__ == '__main__':
    r = 5
    h = 10
    lat, tot = calculate_cylinder_surface_areas(r, h)
    print(f"Lateral surface area: {lat:.4f}")
    print(f"Total surface area: {tot:.4f}")