class HollowSquareBuilder:
    def __init__(self, size, border_char='*', inner_char=' '):
        if size < 1:
            raise ValueError("Size must be at least 1")
        self.size = size
        self.border_char = border_char
        self.inner_char = inner_char

    def build_lines(self):
        for row in range(self.size):
            if row == 0 or row == self.size - 1:
                yield ''.join(self.border_char for _ in range(self.size))
            else:
                yield self.border_char + ''.join(self.inner_char for _ in range(self.size - 2)) + self.border_char

    def get_structure(self):
        return list(self.build_lines())

if __name__ == '__main__':
    builder = HollowSquareBuilder(5, '#', '.')
    lines = builder.get_structure()
    for line in lines:
        print(line)