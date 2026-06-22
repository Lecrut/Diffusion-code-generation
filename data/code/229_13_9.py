class GridPrinter:
    SIZE = 15

    @staticmethod
    def print_grid():
        for i in range(GridPrinter.SIZE):
            for j in range(GridPrinter.SIZE):
                print('*', end=' ')
            print()

if __name__ == '__main__':
    GridPrinter.print_grid()