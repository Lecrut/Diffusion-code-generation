import math

def calculate_cube_volume(edge_length):
    return edge_length ** 3

def calculate_sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

def compare_volumes(cube_edge, sphere_radius):
    cube_vol = calculate_cube_volume(cube_edge)
    sphere_vol = calculate_sphere_volume(sphere_radius)
    return cube_vol > sphere_vol

if __name__ == '__main__':
    cube_edge_length = 4.0
    sphere_radius = 3.0
    is_cube_greater = compare_volumes(cube_edge_length, sphere_radius)
    print(is_cube_greater)