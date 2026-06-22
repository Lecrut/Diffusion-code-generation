def compute_cylinder_areas(radius, height):
    pi = 3.141592653589793
    lateral_surface_area = 2 * pi * radius * height
    total_surface_area = 2 * pi * radius * (radius + height)
    return lateral_surface_area, total_surface_area

if __name__ == '__main__':
    radius = 5
    height = 10
    lateral_area, total_area = compute_cylinder_areas(radius, height)
    print(lateral_area)
    print(total_area)