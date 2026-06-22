class TrianglePrinter:
    ROWS = 5

    @staticmethod
    def print_triangle():
        for i in range(1, TrianglePrinter.ROWS + 1):
            print('*' * i)

if __name__ == '__main__':
    TrianglePrinter.print_triangle()