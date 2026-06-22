class HollowSquareBuilder:
    def __init__(self, size, delimiter='*'):
        self.size = size
        self.delimiter = delimiter

    def build(self):
        if self.size <= 0:
            return iter([])
        if self.size == 1:
            return iter([self.delimiter])
        
        first_line = self.delimiter * self.size
        middle_line = self.delimiter + ' ' * (self.size - 2) + self.delimiter
        
        return iter(
            line for i, line in enumerate(
                [first_line] + [middle_line] * (self.size - 2) + [first_line]
            )
        )

if __name__ == '__main__':
    builder = HollowSquareBuilder(5, '#')
    for line in builder.build():
        print(line)