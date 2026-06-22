import numpy as np

def create_grid():
    return np.array([[i % 2 for i in range(5)] if j % 2 == 0 else [1 - (i % 2) for i in range(5)] for j in range(5)])

if __name__ == '__main__':
    print(create_grid())