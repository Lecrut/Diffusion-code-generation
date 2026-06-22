import math

def get_cylinder_surface_areas(radius, height):
    lateral_area = 2 * math.pi * radius * height
    total_area = 2 * math.pi * radius * (radius + height)
    return lateral_area, total_area

if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    lateral, total = get_cylinder_surface_areas(radius, height)
    print(f"Lateral Surface Area: {lateral:.2f}")
    print(f"Total Surface Area: {total:.2f}")