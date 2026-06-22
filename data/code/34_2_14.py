import math

def compute_cylinder_surface_areas(radius, height):
    lateral_area = 2 * math.pi * radius * height
    base_area = math.pi * radius ** 2
    total_area = lateral_area + 2 * base_area
    return lateral_area, total_area

if __name__ == '__main__':
    r = 3.0
    h = 5.0
    lateral, total = compute_cylinder_surface_areas(r, h)
    print(f"Lateral Area: {lateral}")
    print(f"Total Area: {total}")