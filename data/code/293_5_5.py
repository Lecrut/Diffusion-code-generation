import math

def validate_shape_type(shape_type):
    if shape_type not in ['cube', 'cylinder', 'sphere']:
        raise ValueError("Invalid shape type")

def validate_dimensions(dimensions, expected_length):
    if len(dimensions) != expected_length:
        raise ValueError("Incorrect number of dimensions for the given shape")

def calculate_volume(shape_type, dimensions):
    validate_shape_type(shape_type)
    
    if shape_type == 'cube':
        validate_dimensions(dimensions, 1)
        side = dimensions[0]
        return side ** 3
    elif shape_type == 'cylinder':
        validate_dimensions(dimensions, 2)
        radius, height = dimensions
        return math.pi * radius ** 2 * height
    elif shape_type == 'sphere':
        validate_dimensions(dimensions, 1)
        radius = dimensions[0]
        return (4/3) * math.pi * radius ** 3

if __name__ == '__main__':
    print(calculate_volume('cube', [3]))
    print(calculate_volume('cylinder', [2, 5]))
    print(calculate_volume('sphere', [4]))