class HollowSquareBuilder:
    def __init__(self, size, delimiter='*'):
        if size < 1:
            raise ValueError("Size must be at least 1")
        if not isinstance(delimiter, str) or len(delimiter) != 1:
            raise ValueError("Delimiter must be a single character")
        self.size = size
        self.delimiter = delimiter

    def build(self):
        return self._generate_hollow_square()

    def _generate_hollow_square(self):
        lines = []
        for row in range(self.size):
            if row == 0 or row == self.size - 1:
                yield self.delimiter * self.size
            else:
                yield self.delimiter + (' ' * (self.size - 2)) + self.delimiter

    def get_lines(self):
        return list(self.build())

if __name__ == '__main__':
    builder = HollowSquareBuilder(5, '#')
    result = builder.get_lines()
    for line in result:
        print(line)