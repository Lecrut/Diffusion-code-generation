class HollowSquareBuilder:
    def __init__(self, size, corner_char='+', edge_char='-', inner_space=' '):
        self.size = size
        self.corner_char = corner_char
        self.edge_char = edge_char
        self.inner_space = inner_space

    def build(self):
        if self.size <= 0:
            return ""
        if self.size == 1:
            return self.corner_char

        rows = self._generate_rows()
        return "\n".join(rows)

    def _generate_rows(self):
        return (self._build_row(i) for i in range(self.size))

    def _build_row(self, row_index):
        if self.size == 1:
            return self.corner_char

        if row_index == 0 or row_index == self.size - 1:
            return self._build_edge_row()
        else:
            return self._build_middle_row()

    def _build_edge_row(self):
        if self.size == 1:
            return self.corner_char
        chars = [self.corner_char]
        chars.extend((self.edge_char for _ in range(self.size - 2)))
        chars.append(self.corner_char)
        return "".join(chars)

    def _build_middle_row(self):
        return self.corner_char + (self.inner_space * (self.size - 2)) + self.corner_char

if __name__ == '__main__':
    builder = HollowSquareBuilder(5, '*', '-', ' ')
    result = builder.build()
    print(result)

    builder2 = HollowSquareBuilder(3, '#', '#', '#')
    result2 = builder2.build()
    print(result2)

    builder3 = HollowSquareBuilder(1, 'X', 'X', 'X')
    result3 = builder3.build()
    print(result3)