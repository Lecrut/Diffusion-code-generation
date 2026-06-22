def compute_cylinder_areas(radius, height):
    pi = 3.141592653589793
    lateral_surface_area = 2 * pi * radius * height
    total_surface_area = 2 * pi * radius * (radius + height)
    return lateral_surface_area, total_surface_area

if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    lateral, total = compute_cylinder_areas(radius, height)
    print(lateral)
    print(total)