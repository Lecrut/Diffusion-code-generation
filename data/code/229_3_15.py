class GridPrinter:
    def __init__(self, size):
        self.size = size

    def print_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                print("*", end="")
                if (j + 1) % self.size == 0:
                    print()

if __name__ == '__main__':
    printer = GridPrinter(8)
    printer.print_grid()