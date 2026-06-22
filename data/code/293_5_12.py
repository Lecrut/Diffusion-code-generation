import math

def calculate_cube_volume(side):
    return side ** 3

def calculate_cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

def calculate_sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

def validate_shape_type(shape_type):
    if shape_type not in ['cube', 'cylinder', 'sphere']:
        raise ValueError("Invalid shape type")

def calculate_volume(shape_type, dimensions):
    validate_shape_type(shape_type)
    
    if shape_type == 'cube':
        return calculate_cube_volume(dimensions[0])
    elif shape_type == 'cylinder':
        return calculate_cylinder_volume(*dimensions)
    elif shape_type == 'sphere':
        return calculate_sphere_volume(dimensions[0])

if __name__ == '__main__':
    cube_volume = calculate_volume('cube', [2])
    cylinder_volume = calculate_volume('cylinder', [3, 7])
    sphere_volume = calculate_volume('sphere', [5])

    print(cube_volume)
    print(cylinder_volume)
    print(sphere_volume)