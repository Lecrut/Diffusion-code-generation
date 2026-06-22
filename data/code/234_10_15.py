import numpy as np

def generate_checkerboard(size=8):
    return np.fromfunction(lambda i, j: (i + j) % 2, (size, size), dtype=int)

if __name__ == '__main__':
    checkerboard = generate_checkerboard()
    print(checkerboard)