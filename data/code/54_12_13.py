class HollowSquare:
    def __init__(self, size, delimiter='*'):
        self.size = size
        self.delimiter = delimiter

    def _generate_row(self, row_index, total_rows):
        if row_index == 0 or row_index == total_rows - 1:
            return self.delimiter * self.size
        if 0 < row_index < total_rows - 1:
            return self.delimiter + (' ' * (self.size - 2)) + self.delimiter
        return ''

    def build(self):
        if self.size <= 0:
            return ''
        if self.size == 1:
            return self.delimiter
        rows = (self._generate_row(i, self.size) for i in range(self.size))
        return '\n'.join(rows)

if __name__ == '__main__':
    square = HollowSquare(5, '#')
    print(square.build())