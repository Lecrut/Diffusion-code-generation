import math

SHAPE_VOLUMES = {
    'cube': lambda dimensions: dimensions[0] ** 3,
    'cylinder': lambda dimensions: math.pi * dimensions[0] ** 2 * dimensions[1],
    'sphere': lambda dimensions: (4/3) * math.pi * dimensions[0] ** 3
}

def calculate_volume(shape_type, dimensions):
    return SHAPE_VOLUMES.get(shape_type, lambda _: None)(dimensions)

if __name__ == '__main__':
    print(calculate_volume('cube', [3]))
    print(calculate_volume('cylinder', [2, 5]))
    print(calculate_volume('sphere', [4]))