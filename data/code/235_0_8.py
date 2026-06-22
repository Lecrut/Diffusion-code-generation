class TrianglePattern:
    HEIGHT = 5

    @staticmethod
    def print_triangle():
        height = TrianglePattern.HEIGHT
        for i in range(1, height + 1):
            print('*' * i)

if __name__ == '__main__':
    TrianglePattern.print_triangle()