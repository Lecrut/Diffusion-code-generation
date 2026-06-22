import math

def calculate_sphere_surface_area(radius):
    return 4 * math.pi * radius**2

def calculate_cube_surface_area(side_length):
    return 6 * side_length**2

if __name__ == '__main__':
    sphere_radius = 5.0
    cube_side = 5.0
    
    try:
        sphere_area = calculate_sphere_surface_area(sphere_radius)
        cube_area = calculate_cube_surface_area(cube_side)
        
        print(f"Sphere Surface Area: {sphere_area}")
        print(f"Cube Surface Area: {cube_area}")
        
        if math.isclose(sphere_area, cube_area, rel_tol=1e-9):
            print("The surface areas are equal.")
        else:
            difference = abs(sphere_area - cube_area)
            print(f"The surface areas differ by: {difference}")
    
    except TypeError as e:
        print(f"Invalid input: {e}")