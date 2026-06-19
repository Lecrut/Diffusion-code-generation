import math

def calculate_cube_volume(edge_length):
    if edge_length <= 0:
        return 0
    return edge_length ** 3

def calculate_sphere_volume(radius):
    if radius <= 0:
        return 0
    return (4/3) * math.pi * (radius ** 3)

def is_cube_volume_greater(cube_edge, sphere_radius):
    cube_volume = calculate_cube_volume(cube_edge)
    sphere_volume = calculate_sphere_volume(sphere_radius)
    return cube_volume > sphere_volume

if __name__ == '__main__':
    cube_edge_length = 3
    sphere_radius = 2
    result = is_cube_volume_greater(cube_edge_length, sphere_radius)
    print(result)