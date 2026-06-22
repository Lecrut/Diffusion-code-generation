import math

def calculate_volume(shape_type, dimensions):
    if not isinstance(dimensions, (list, tuple)) or len(dimensions) != 1 and shape_type == 'cube':
        raise ValueError("Invalid dimensions for cube")
    if not isinstance(dimensions, (list, tuple)) or len(dimensions) != 2 and shape_type == 'cylinder':
        raise ValueError("Invalid dimensions for cylinder")
    if not isinstance(dimensions, (list, tuple)) or len(dimensions) != 1 and shape_type == 'sphere':
        raise ValueError("Invalid dimensions for sphere")

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