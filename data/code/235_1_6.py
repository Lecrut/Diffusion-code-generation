class SquareBox:
    SIZE = 4

    @staticmethod
    def print_box():
        pattern = '#' * SquareBox.SIZE
        for _ in range(SquareBox.SIZE):
            print(pattern)

if __name__ == '__main__':
    SquareBox.print_box()