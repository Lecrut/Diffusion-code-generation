import math

def sphere_surface_area(radius):
    return 4 * math.pi * radius ** 2

def cube_surface_area(side_length):
    return 6 * side_length ** 2

if __name__ == '__main__':
    sphere_radius = 5.0
    cube_side_length = 3.0
    
    sphere_area = sphere_surface_area(sphere_radius)
    cube_area = cube_surface_area(cube_side_length)
    
    print(f"Sphere surface area: {sphere_area:.2f}")
    print(f"Cube surface area: {cube_area:.2f}")
    
    if math.isclose(sphere_area, cube_area, rel_tol=1e-9):
        print("The surface areas are approximately equal.")
    else:
        print("The surface areas are not equal.")