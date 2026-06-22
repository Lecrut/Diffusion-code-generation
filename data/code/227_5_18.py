class TrianglePrinter:
    MAX_HEIGHT = 5

    @staticmethod
    def print_triangle(height):
        pattern = [('*' * i) for i in range(1, height + 1)]
        for line in pattern:
            print(line)

if __name__ == '__main__':
    triangle_printer = TrianglePrinter()
    triangle_printer.print_triangle(TrianglePrinter.MAX_HEIGHT)