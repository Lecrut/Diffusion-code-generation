import numpy as np

checkerboard_map = {True: 1, False: 0}

def generate_checkerboard(size=8):
    return (np.arange(size)[:, None] + np.arange(size)) % 2 == 0

if __name__ == '__main__':
    board = generate_checkerboard(8)
    for row in board:
        print(" ".join(str(cell) for cell in row))