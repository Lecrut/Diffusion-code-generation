import matplotlib.pyplot as plt
import numpy as np

class Checkerboard:
    def __init__(self, size=8):
        self.size = size
        self.board = self.generate_checkerboard()

    def generate_checkerboard(self):
        checkerboard = np.zeros((self.size, self.size), dtype=int)
        for i in range(self.size):
            for j in range(self.size):
                if (i + j) % 2 == 0:
                    checkerboard[i, j] = 1
        return checkerboard

    def display_checkerboard(self):
        plt.imshow(self.board, cmap='gray')
        plt.axis('off')
        plt.show()

if __name__ == '__main__':
    cb = Checkerboard()
    cb.display_checkerboard()