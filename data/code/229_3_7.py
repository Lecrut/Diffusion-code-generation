class SquareGrid:
    SIZE = 8

    @staticmethod
    def print_grid():
        for _ in range(SquareGrid.SIZE):
            print('*' * SquareGrid.SIZE)

if __name__ == '__main__':
    SquareGrid.print_grid()