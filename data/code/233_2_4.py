import numpy as np

def fill_with_at(rows, cols):
    return np.full((rows, cols), '@', dtype=str)

if __name__ == '__main__':
    result = fill_with_at(5, 10)
    print(result)