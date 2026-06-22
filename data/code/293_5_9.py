import math

def calculate_volume(shape_type, dimensions):
    if shape_type == 'cube':
        side = dimensions[0]
        return side ** 3
    elif shape_type == 'cylinder':
        radius, height = dimensions
        return math.pi * (radius ** 2) * height
    elif shape_type == 'sphere':
        radius = dimensions[0]
        return (4/3) * math.pi * (radius ** 3)
    else:
        raise ValueError("Invalid shape type")

if __name__ == '__main__':
    print(calculate_volume('cube', [2]))
    print(calculate_volume('cylinder', [3, 5]))
    print(calculate_volume('sphere', [4]))