STAR_CHAR = '*'
GRID_SIZE = 10
LINE_WIDTH = GRID_SIZE

class StarSquarePrinter:
    def __init__(self, size):
        self.size = size
        self.line_pattern = STAR_CHAR * size

    def print_grid(self):
        for _ in range(self.size):
            print(self.line_pattern)

if __name__ == '__main__':
    printer = StarSquarePrinter(GRID_SIZE)
    printer.print_grid()