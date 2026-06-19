import math

def compare_volumes():
    cube_edge = 3
    sphere_radius = 2
    
    cube_volume = cube_edge ** 3
    sphere_volume = (4/3) * math.pi * (sphere_radius ** 3)
    
    return cube_volume > sphere_volume

if __name__ == '__main__':
    result = compare_volumes()
    print(result)