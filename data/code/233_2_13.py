import numpy as np

def fill_rectangular_area(width, height):
    return np.full((height, width), '@', dtype=str)

if __name__ == '__main__':
    result = fill_rectangular_area(5, 3)
    print(result)