class GridPrinter:
    def __init__(self, size):
        self.size = size

    def print_grid(self):
        for i in range(self.size):
            row = ''.join('*' if j % 2 == 0 else ' ' for j in range(self.size))
            print(row)

if __name__ == '__main__':
    printer = GridPrinter(15)
    printer.print_grid()