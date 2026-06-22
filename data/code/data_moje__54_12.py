class HollowSquareBuilder:
    def __init__(self, size: int, char: str = '*'):
        self.size = size
        self.char = char

    def build(self) -> str:
        if self.size < 1:
            return ''
        lines = (
            self._generate_line(i)
            for i in range(self.size)
        )
        return '\n'.join(lines)

    def _generate_line(self, row_index: int) -> str:
        if row_index == 0 or row_index == self.size - 1:
            return self.char * self.size
        inner_width = self.size - 2
        return self.char + ' ' * inner_width + self.char

if __name__ == '__main__':
    builder = HollowSquareBuilder(5, '#')
    result = builder.build()
    print(result)