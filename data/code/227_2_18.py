class InvertedTriangle:
    MAX_ROWS = 6

    @staticmethod
    def print_triangle(rows=MAX_ROWS):
        for i in range(rows, 0, -1):
            print('*' * i)

if __name__ == '__main__':
    InvertedTriangle.print_triangle()