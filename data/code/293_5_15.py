import math

def validate_dimensions(shape_type, dimensions):
    if shape_type == 'cube':
        return len(dimensions) == 1 and isinstance(dimensions[0], (int, float)) and dimensions[0] > 0
    elif shape_type == 'cylinder':
        return len(dimensions) == 2 and all(isinstance(x, (int, float)) for x in dimensions) and all(x > 0 for x in dimensions)
    elif shape_type == 'sphere':
        return len(dimensions) == 1 and isinstance(dimensions[0], (int, float)) and dimensions[0] > 0
    return False

def calculate_volume(shape_type, dimensions):
    if not validate_dimensions(shape_type, dimensions):
        raise ValueError("Invalid dimensions for the specified shape")
    if shape_type == 'cube':
        side = dimensions[0]
        return side ** 3
    elif shape_type == 'cylinder':
        radius, height = dimensions
        return math.pi * radius ** 2 * height
    elif shape_type == 'sphere':
        radius = dimensions[0]
        return (4/3) * math.pi * radius ** 3

if __name__ == '__main__':
    print(calculate_volume('cube', [3]))
    print(calculate_volume('cylinder', [2, 5]))
    print(calculate_volume('sphere', [4]))