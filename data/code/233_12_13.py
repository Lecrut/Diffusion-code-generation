import numpy as np

def create_ascii_rectangle(width, height):
    rectangle = np.full((height, width), '#', dtype=str)
    return rectangle

if __name__ == '__main__':
    sample_width = 10
    sample_height = 5
    ascii_art = create_ascii_rectangle(sample_width, sample_height)
    print('\n'.join(' '.join(row) for row in ascii_art))