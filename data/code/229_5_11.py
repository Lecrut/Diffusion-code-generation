import numpy as np

class GridGenerator:
    @staticmethod
    def create_square_grid(side_length):
        return np.arange(side_length * side_length).reshape((side_length, side_length))

if __name__ == '__main__':
    grid = GridGenerator.create_square_grid(4)
    print(grid)