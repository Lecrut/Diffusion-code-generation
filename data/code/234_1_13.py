import numpy as np

class CheckerboardGenerator:
    def __init__(self, size):
        self.size = size
        self.board = None
    
    def generate_board(self):
        indices = np.arange(self.size)
        board = (indices[:, None] + indices) % 2 == 0
        self.board = board.astype(int)
    
    def get_board(self):
        return self.board

if __name__ == '__main__':
    generator = CheckerboardGenerator(8)
    generator.generate_board()
    checkerboard = generator.get_board()
    print(checkerboard)