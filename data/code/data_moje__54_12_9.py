class HollowSquareBuilder:
    def __init__(self, side_length, fill_char='*', border_char=None):
        if side_length < 1:
            raise ValueError("Side length must be at least 1")
        self.side_length = side_length
        self.fill_char = fill_char
        self.border_char = border_char if border_char is not None else fill_char

    def build(self):
        if self.side_length == 1:
            yield self.border_char
            return

        for row_idx in range(self.side_length):
            if row_idx == 0 or row_idx == self.side_length - 1:
                line = self.border_char * self.side_length
            else:
                line = (
                    self.border_char +
                    (self.fill_char * (self.side_length - 2)) +
                    self.border_char
                ) if self.side_length > 2 else self.border_char * self.side_length
            yield line

if __name__ == '__main__':
    builder = HollowSquareBuilder(5, fill_char=' ', border_char='#')
    result = list(builder.build())
    print('\n'.join(result))

    builder2 = HollowSquareBuilder(1, fill_char='X', border_char='O')
    result2 = list(builder2.build())
    print('\n'.join(result2))

    builder3 = HollowSquareBuilder(3, fill_char='-', border_char='+')
    result3 = list(builder3.build())
    print('\n'.join(result3))