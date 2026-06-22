class PyramidPrinter:
    NUM_ROWS = 5

    @staticmethod
    def print_inverted_pyramid():
        num_rows = PyramidPrinter.NUM_ROWS
        for i in range(num_rows, 0, -1):
            spaces = ' ' * (num_rows - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)

if __name__ == '__main__':
    PyramidPrinter.print_inverted_pyramid()