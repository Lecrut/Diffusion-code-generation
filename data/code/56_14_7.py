import math

def calculate_volumes():
    cube_edge_length = 3
    sphere_radius = 2
    
    cube_volume = cube_edge_length ** 3
    sphere_volume = (4/3) * math.pi * (sphere_radius ** 3)
    
    return cube_volume > sphere_volume

if __name__ == '__main__':
    result = calculate_volumes()
    print(result)