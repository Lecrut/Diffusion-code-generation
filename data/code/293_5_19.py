import math

def validate_shape_type(shape_type):
    if shape_type not in ['cube', 'cylinder', 'sphere']:
        raise ValueError("Invalid shape type")

def calculate_volume(shape_type, dimensions):
    validate_shape_type(shape_type)
    
    if shape_type == 'cube':
        side = dimensions[0]
        return side ** 3
    elif shape_type == 'cylinder':
        radius, height = dimensions
        return math.pi * radius ** 2 * height
    else:
        radius = dimensions[0]
        return (4/3) * math.pi * radius ** 3

if __name__ == '__main__':
    print(calculate_volume('cube', [3]))
    print(calculate_volume('cylinder', [2, 5]))
    print(calculate_volume('sphere', [4]))