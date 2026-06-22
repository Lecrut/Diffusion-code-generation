class StarTriangle:
    def __init__(self, rows):
        self.rows = rows

    def print_triangle(self):
        for i in range(self.rows, 0, -1):
            print('*' * i)

if __name__ == '__main__':
    triangle_printer = StarTriangle(6)
    triangle_printer.print_triangle()