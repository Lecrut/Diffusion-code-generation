import numpy as np

class CheckerboardGenerator:
    CHECKERBOARD_SIZE = 8
    EMPTY = 0
    FILLED = 1
    
    @staticmethod
    def generate_checkerboard():
        board = np.zeros((CheckerboardGenerator.CHECKERBOARD_SIZE, CheckerboardGenerator.CHECKERBOARD_SIZE), dtype=int)
        for i in range(CheckerboardGenerator.CHECKERBOARD_SIZE):
            for j in range(CheckerboardGenerator.CHECKERBOARD_SIZE):
                if (i + j) % 2 == 0:
                    board[i, j] = CheckerboardGenerator.EMPTY
                else:
                    board[i, j] = CheckerboardGenerator.FILLED
        return board

if __name__ == '__main__':
    checkerboard = CheckerboardGenerator.generate_checkerboard()
    print(checkerboard)