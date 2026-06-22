import numpy as np

class CheckerboardGenerator:
    def __init__(self, size):
        self.size = size
        self.board = None

    def generate(self):
        indices = np.arange(self.size)
        row_indices, col_indices = np.meshgrid(indices, indices, indexing='ij')
        self.board = (row_indices + col_indices) % 2 == 0

    def get_board(self):
        return self.board

if __name__ == '__main__':
    generator = CheckerboardGenerator(8)
    generator.generate()
    print(generator.get_board())