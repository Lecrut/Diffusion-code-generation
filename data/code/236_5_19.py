import numpy as np

def tile_square(base_array, num_tiles):
    return np.tile(base_array, (num_tiles, num_tiles))

if __name__ == '__main__':
    base = np.array([[1, 2], [3, 4]])
    tiles = 3
    result = tile_square(base, tiles)
    print(result)