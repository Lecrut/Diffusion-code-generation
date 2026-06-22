class StarTriangle:
    MAX_ROWS = 5

    @staticmethod
    def print_triangle():
        triangle_pattern = '\n'.join(['*' * i for i in range(1, StarTriangle.MAX_ROWS + 1)])
        print(triangle_pattern)

if __name__ == '__main__':
    StarTriangle.print_triangle()