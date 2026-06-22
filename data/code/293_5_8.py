import math

VOLUME_CONSTANTS = {
    'cube': lambda side: side ** 3,
    'cylinder': lambda radius, height: math.pi * radius ** 2 * height,
    'sphere': lambda radius: (4/3) * math.pi * radius ** 3
}

def calculate_volume(shape_type, dimensions):
    if shape_type not in VOLUME_CONSTANTS:
        raise ValueError("Invalid shape type")
    return VOLUME_CONSTANTS[shape_type](*dimensions)

if __name__ == '__main__':
    print(calculate_volume('cube', [3]))
    print(calculate_volume('cylinder', [2, 5]))
    print(calculate_volume('sphere', [4]))