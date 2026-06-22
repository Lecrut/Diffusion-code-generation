import numpy as np

def create_ascii_rectangle(width, height, fill_char='#'):
    rectangle = np.full((height, width), fill_char, dtype=str)
    return rectangle

if __name__ == '__main__':
    rect = create_ascii_rectangle(10, 5)
    print('\n'.join(' '.join(row) for row in rect))