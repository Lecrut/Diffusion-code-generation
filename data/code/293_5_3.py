import math

def calculate_volume(shape_type, dimensions):
    if shape_type == 'cube':
        side = dimensions[0]
        volume = side ** 3
    elif shape_type == 'cylinder':
        radius, height = dimensions
        volume = math.pi * radius ** 2 * height
    elif shape_type == 'sphere':
        radius = dimensions[0]
        volume = (4/3) * math.pi * radius ** 3
    else:
        raise ValueError("Invalid shape type")
    return volume

if __name__ == '__main__':
    cube_volume = calculate_volume('cube', [2])
    cylinder_volume = calculate_volume('cylinder', [3, 7])
    sphere_volume = calculate_volume('sphere', [5])

    print(f"Cube Volume: {cube_volume}")
    print(f"Cylinder Volume: {cylinder_volume}")
    print(f"Sphere Volume: {sphere_volume}")