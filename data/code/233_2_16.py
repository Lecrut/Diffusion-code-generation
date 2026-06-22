import numpy as np

def fill_rectangle(width, height):
    return np.full((height, width), '@', dtype=str)

if __name__ == '__main__':
    rectangle = fill_rectangle(5, 3)
    print(rectangle)