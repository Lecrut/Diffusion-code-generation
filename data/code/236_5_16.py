import numpy as np

def tile_square(base_array, repeat_count):
    return np.tile(base_array, (repeat_count, repeat_count))

if __name__ == '__main__':
    base = np.array([[1, 2], [3, 4]])
    repeated = tile_square(base, 3)
    print(repeated)