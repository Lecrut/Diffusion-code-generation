import numpy as np

def checkerboard(N):
    return (np.arange(N).reshape(-1, 1) % 2 + np.arange(N) % 2) % 2

if __name__ == '__main__':
    print(checkerboard(8))