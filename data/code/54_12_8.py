class HollowSquareBuilder:
    def __init__(self, size, char='#'):
        if size < 1:
            raise ValueError("Size must be at least 1")
        if not char:
            raise ValueError("Delimiter character cannot be empty")
        self.size = size
        self.char = char

    def build(self):
        if self.size == 1:
            return self.char
        top_bottom = self.char * self.size
        middle_width = self.size - 2
        middle_row = self.char + ' ' * middle_width + self.char
        return [
            top_bottom if i == 0 or i == self.size - 1 else middle_row
            for i in range(self.size)
        ]

if __name__ == '__main__':
    builder = HollowSquareBuilder(5, '*')
    result = builder.build()
    for line in result:
        print(line)
    builder_small = HollowSquareBuilder(1, 'X')
    print(builder_small.build())