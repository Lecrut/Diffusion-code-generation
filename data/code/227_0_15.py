class TrianglePattern:
    @staticmethod
    def print_triangle(rows):
        for i in range(1, rows + 1):
            print('*' * i)

if __name__ == '__main__':
    TRIANGLE_ROWS = 5
    TrianglePattern.print_triangle(TRIANGLE_ROWS)