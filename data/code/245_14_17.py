import math

def calculate_sphere_surface_area(radius):
    return 4 * math.pi * radius**2

def calculate_cube_surface_area(side_length):
    return 6 * side_length**2

if __name__ == '__main__':
    sphere_radius = 3.5
    cube_side_length = 4.0
    
    sphere_surface_area = calculate_sphere_surface_area(sphere_radius)
    cube_surface_area = calculate_cube_surface_area(cube_side_length)
    
    print(f"Sphere Surface Area: {sphere_surface_area}")
    print(f"Cube Surface Area: {cube_surface_area}")
    
    if math.isclose(sphere_surface_area, cube_surface_area, rel_tol=1e-9):
        print("The surface areas are equal.")
    else:
        difference = abs(sphere_surface_area - cube_surface_area)
        print(f"The surface areas differ by: {difference}")