import math

def calculate_sphere_surface_area(radius):
    return 4 * math.pi * radius ** 2

def calculate_cube_surface_area(side_length):
    return 6 * side_length ** 2

def compare_surface_areas(sphere_radius, cube_side_length):
    sphere_area = calculate_sphere_surface_area(sphere_radius)
    cube_area = calculate_cube_surface_area(cube_side_length)
    
    if math.isclose(sphere_area, cube_area, rel_tol=1e-9):
        return "The surface areas are equal."
    elif sphere_area > cube_area:
        return "The sphere has a larger surface area."
    else:
        return "The cube has a larger surface area."

if __name__ == '__main__':
    print(compare_surface_areas(5, 3))