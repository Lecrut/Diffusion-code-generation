import numpy as np

def tile_square_pattern(base_shape=(2, 2), repeat_count=3):
    base_array = np.tile(np.array(['##', '##']), (base_shape[0], base_shape[1]))
    tiled_pattern = np.tile(base_array, (repeat_count, repeat_count))
    return tiled_pattern.flatten().reshape((repeat_count * base_shape[0], repeat_count * base_shape[1]))

if __name__ == '__main__':
    pattern = tile_square_pattern()
    for row in pattern:
        print("".join(row))