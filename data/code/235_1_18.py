class BoxPattern:
    def __init__(self, size):
        self.size = size

    def print_box(self):
        pattern = '#' * self.size
        for _ in range(self.size):
            print(pattern)

if __name__ == '__main__':
    box = BoxPattern(4)
    box.print_box()