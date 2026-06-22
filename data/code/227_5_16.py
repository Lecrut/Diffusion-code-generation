class TrianglePrinter:
    MAX_HEIGHT = 5

    @staticmethod
    def print_triangle(height):
        for i in range(1, height + 1):
            print('*' * i)

if __name__ == '__main__':
    TrianglePrinter.print_triangle(TrianglePrinter.MAX_HEIGHT)