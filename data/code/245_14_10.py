import math

def compare_surface_areas(radius, side_length):
    sphere_area = 4 * math.pi * radius ** 2
    cube_area = 6 * side_length ** 2
    return sphere_area, cube_area

if __name__ == '__main__':
    sample_radius = 5.0
    sample_side_length = 3.0
    sphere_surface, cube_surface = compare_surface_areas(sample_radius, sample_side_length)
    print(f"Sphere surface area: {sphere_surface}")
    print(f"Cube surface area: {cube_surface}")