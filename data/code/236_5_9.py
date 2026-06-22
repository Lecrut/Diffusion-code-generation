import numpy as np

def tile_square(base_array, repetitions):
    tiled_array = np.tile(base_array, (repetitions, repetitions))
    return tiled_array

if __name__ == '__main__':
    base_array = np.array([[1, 2], [3, 4]])
    repetitions = 3
    result = tile_square(base_array, repetitions)
    print(result)