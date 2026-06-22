import numpy as np

class CheckerboardGenerator:
    def __init__(self, size):
        self.size = size
        self.board = self.generate_checkerboard()

    def generate_checkerboard(self):
        return (np.arange(self.size)[:, None] + np.arange(self.size)) % 2 == 0

if __name__ == '__main__':
    checkerboard_gen = CheckerboardGenerator(8)
    print(checkerboard_gen.board)