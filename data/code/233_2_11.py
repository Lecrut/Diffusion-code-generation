import numpy as np

def fill_rectangle(width, height):
    return np.full((height, width), '@', dtype=str)

if __name__ == '__main__':
    sample_width = 7
    sample_height = 5
    filled_rectangle = fill_rectangle(sample_width, sample_height)
    print('\n'.join(''.join(row) for row in filled_rectangle))