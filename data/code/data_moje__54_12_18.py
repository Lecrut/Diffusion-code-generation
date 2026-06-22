class HollowSquareBuilder:
    def __init__(self, size, top_char='*', bottom_char='*', side_char='|', empty_char=' '):
        self.size = size
        self.top_char = top_char
        self.bottom_char = bottom_char
        self.side_char = side_char
        self.empty_char = empty_char

    def build(self):
        if self.size <= 0:
            return ""
        if self.size == 1:
            return self.top_char
        if self.size == 2:
            row = self.top_char * 2
            return row + '\n' + row
        lines = (
            self.top_char * self.size if i == 0
            else self.bottom_char * self.size if i == self.size - 1
            else self.side_char + self.empty_char * (self.size - 2) + self.side_char
            for i in range(self.size)
        )
        return '\n'.join(lines)

if __name__ == '__main__':
    builder = HollowSquareBuilder(5, '+', '+', '-', '.')
    result = builder.build()
    print(result)