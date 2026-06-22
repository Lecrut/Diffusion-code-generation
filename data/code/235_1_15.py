class BoxPattern:
    SIZE = 4

    @staticmethod
    def print_pattern():
        pattern = '#' * BoxPattern.SIZE
        for _ in range(BoxPattern.SIZE):
            print(pattern)

if __name__ == '__main__':
    BoxPattern.print_pattern()