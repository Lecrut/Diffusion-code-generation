import math

def calculate_cube_volume(edge_length):
    if edge_length <= 0:
        raise ValueError("Edge length must be positive")
    return edge_length ** 3

def calculate_sphere_volume(radius):
    if radius <= 0:
        raise ValueError("Radius must be positive")
    return (4/3) * math.pi * (radius ** 3)

def is_cube_volume_greater(edge_length, radius):
    cube_volume = calculate_cube_volume(edge_length)
    sphere_volume = calculate_sphere_volume(radius)
    return cube_volume > sphere_volume

if __name__ == '__main__':
    edge_length = 3
    radius = 2
    result = is_cube_volume_greater(edge_length, radius)
    print(result)