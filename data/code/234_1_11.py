import numpy as np

def checkerboard(N):
    return (np.arange(N).reshape(-1, 1) + np.arange(N)) % 2 == 0

if __name__ == '__main__':
    print(checkerboard(8))