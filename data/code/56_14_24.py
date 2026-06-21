import math

CUBE_EDGE_LENGTH = 3
SPHERE_RADIUS = 2

def calculate_cube_volume(edge_length):
    return edge_length ** 3

def calculate_sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

def is_cube_volume_greater(edge_length, radius):
    cube_volume = calculate_cube_volume(edge_length)
    sphere_volume = calculate_sphere_volume(radius)
    return cube_volume > sphere_volume

if __name__ == '__main__':
    result = is_cube_volume_greater(CUBE_EDGE_LENGTH, SPHERE_RADIUS)
    print(result)