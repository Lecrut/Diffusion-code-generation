import numpy as np

def tile_square(base_array, num_tiles):
    tiled_array = np.tile(base_array, (num_tiles, num_tiles))
    return tiled_array

if __name__ == '__main__':
    base_array = np.array([[1, 2], [3, 4]])
    num_tiles = 3
    result = tile_square(base_array, num_tiles)
    print(result)