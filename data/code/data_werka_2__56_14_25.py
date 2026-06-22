import math

def calculate_cube_volume(edge_length):
    return edge_length ** 3

def calculate_sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

def is_cube_volume_greater_than_sphere(cube_edge_length, sphere_radius):
    cube_vol = calculate_cube_volume(cube_edge_length)
    sphere_vol = calculate_sphere_volume(sphere_radius)
    return cube_vol > sphere_vol

if __name__ == '__main__':
    sample_cube_edge_length = 4
    sample_sphere_radius = 2.5
    result = is_cube_volume_greater_than_sphere(sample_cube_edge_length, sample_sphere_radius)
    print(result)