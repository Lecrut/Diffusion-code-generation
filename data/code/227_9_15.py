class StarTriangle:
    ROWS = 4

    @staticmethod
    def print_triangle():
        for i in range(1, StarTriangle.ROWS + 1):
            print('*' * i)

if __name__ == '__main__':
    StarTriangle.print_triangle()