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
    
    print(f"Sphere surface area: {sphere_area}")
    print(f"Cube surface area: {cube_area}")
    
    if math.isclose(sphere_area, cube_area):
        print("The surface areas are equal.")
    else:
        print("The surface areas are not equal.")