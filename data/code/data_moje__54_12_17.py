class HollowSquareBuilder:
    def __init__(self, side_length, character='*', delimiter=' '):
        if side_length < 1:
            raise ValueError("Side length must be at least 1")
        self.side_length = side_length
        self.character = character
        self.delimiter = delimiter

    def build(self):
        def row_generator(row_index):
            if self.side_length == 1:
                return self.character
            if row_index == 0 or row_index == self.side_length - 1:
                return self.delimiter.join([self.character] * self.side_length)
            inner_spaces = self.delimiter.join([''] * (self.side_length - 2))
            return self.delimiter.join([self.character, inner_spaces, self.character])

        return '\n'.join(row_generator(i) for i in range(self.side_length))

if __name__ == '__main__':
    builder = HollowSquareBuilder(5, '#', '-')
    print(builder.build())