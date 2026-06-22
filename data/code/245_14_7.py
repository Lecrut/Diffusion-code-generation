import math

def sphere_surface_area(radius):
    return 4 * math.pi * radius ** 2

def cube_surface_area(side_length):
    return 6 * side_length ** 2

def compare_areas(sphere_radius, cube_side_length):
    sphere_area = sphere_surface_area(sphere_radius)
    cube_area = cube_surface_area(cube_side_length)
    
    if abs(sphere_area - cube_area) < 1e-9:
        return "Areas are equal"
    elif sphere_area > cube_area:
        return "Sphere area is greater"
    else:
        return "Cube area is greater"

if __name__ == '__main__':
    print(compare_areas(5, 3))