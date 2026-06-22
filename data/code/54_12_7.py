class HollowSquareBuilder:
    def __init__(self, side_length, delimiter=' '):
        if side_length < 1:
            raise ValueError("Side length must be at least 1")
        self.side_length = side_length
        self.delimiter = delimiter

    def build(self):
        if self.side_length == 1:
            return self.delimiter
        rows = self._generate_rows()
        return '\n'.join(rows)

    def _generate_rows(self):
        row_gen = (self._build_row(i) for i in range(self.side_length))
        return list(row_gen)

    def _build_row(self, row_index):
        if row_index == 0 or row_index == self.side_length - 1:
            return self._fill_row()
        else:
            return self._border_char() + self.delimiter * (self.side_length - 2) + self._border_char()

    def _fill_row(self):
        return self._border_char() * self.side_length

    def _border_char(self):
        return '*'

if __name__ == '__main__':
    builder = HollowSquareBuilder(5, '-')
    result = builder.build()
    print(result)

    builder2 = HollowSquareBuilder(3, '*')
    result2 = builder2.build()
    print(result2)

    builder3 = HollowSquareBuilder(1, '#')
    result3 = builder3.build()
    print(result3)