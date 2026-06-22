import numpy as np

def tile_square(base_array, repeat_count):
    tiled_array = np.tile(base_array, (repeat_count, repeat_count))
    return tiled_array

if __name__ == '__main__':
    base_array = np.array([[1, 2], [3, 4]])
    repeat_count = 3
    result = tile_square(base_array, repeat_count)
    print(result)