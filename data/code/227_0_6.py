class TrianglePrinter:
    def __init__(self, rows):
        self.rows = rows

    def print_triangle(self):
        for i in range(1, self.rows + 1):
            print('*' * i)

if __name__ == '__main__':
    printer = TrianglePrinter(5)
    printer.print_triangle()