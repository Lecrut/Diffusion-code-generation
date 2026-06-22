class StarTriangle:
    ROWS = 4

    @staticmethod
    def print_triangle(rows=ROWS):
        for i in range(1, rows + 1):
            print('*' * i)

if __name__ == '__main__':
    triangle = StarTriangle()
    triangle.print_triangle()