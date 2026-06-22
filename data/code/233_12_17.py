import numpy as np

def create_filled_rectangle(width, height):
    return np.full((height, width), '#')

if __name__ == '__main__':
    rectangle = create_filled_rectangle(10, 5)
    print(rectangle)