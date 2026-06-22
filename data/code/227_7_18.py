class PyramidPrinter:
    def __init__(self, rows):
        self.rows = rows

    def print_pyramid(self):
        for i in range(1, self.rows + 1):
            spaces = " " * (self.rows - i)
            stars = "*" * (2 * i - 1)
            print(spaces + stars)

if __name__ == '__main__':
    printer = PyramidPrinter(5)
    printer.print_pyramid()