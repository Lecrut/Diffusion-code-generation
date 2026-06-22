import math

def sphere_surface_area(radius):
    return 4 * math.pi * radius ** 2

def cube_surface_area(side_length):
    return 6 * side_length ** 2

def compare_areas():
    sphere_radius = 5.0
    cube_side_length = 3.0
    
    sphere_area = sphere_surface_area(sphere_radius)
    cube_area = cube_surface_area(cube_side_length)
    
    if math.isclose(sphere_area, cube_area):
        print("The surface areas are equal.")
    elif sphere_area > cube_area:
        print(f"The sphere has a larger surface area by {sphere_area - cube_area:.2f}.")
    else:
        print(f"The cube has a larger surface area by {cube_area - sphere_area:.2f}.")

if __name__ == '__main__':
    compare_areas()