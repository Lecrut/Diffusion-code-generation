import numpy as np

def create_square_grid():
    return np.array([[i % 2 for i in range(5)] for _ in range(5)])

if __name__ == '__main__':
    print(create_square_grid())