import numpy as np

def generate_checkerboard():
    checkerboard = np.zeros((8, 8), dtype=int)
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                checkerboard[i, j] = 1
    return checkerboard

if __name__ == '__main__':
    print(generate_checkerboard())