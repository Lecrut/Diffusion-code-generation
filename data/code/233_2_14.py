import numpy as np

def fill_rectangle(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be greater than zero.")
    
    rectangle = np.full((height, width), '@', dtype=str)
    return rectangle

if __name__ == '__main__':
    result = fill_rectangle(5, 3)
    print(result)