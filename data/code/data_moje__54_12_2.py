class HollowSquareBuilder:
    def __init__(self, size, delimiter=' ', inner_char=' ', border_char='*'):
        self.size = size
        self.delimiter = delimiter
        self.inner_char = inner_char
        self.border_char = border_char

    def build(self):
        if self.size < 1:
            return ""
        if self.size == 1:
            return self.border_char
        def row_generator():
            top_bottom_row = self.delimiter.join([self.border_char] * self.size)
            middle_row = self.delimiter.join(
                [self.border_char] + [self.inner_char] * (self.size - 2) + [self.border_char]
            )
            yield top_bottom_row
            for _ in range(self.size - 2):
                yield middle_row
            yield top_bottom_row
        return "\n".join(row_generator())

if __name__ == '__main__':
    builder = HollowSquareBuilder(5, delimiter='', inner_char=' ', border_char='#')
    print(builder.build())
    builder2 = HollowSquareBuilder(3, delimiter=',', inner_char='.', border_char='O')
    print(builder2.build())
    builder3 = HollowSquareBuilder(1, delimiter=' ', inner_char='x', border_char='@')
    print(builder3.build())
    builder4 = HollowSquareBuilder(7, delimiter='|', inner_char='-', border_char='+')
    print(builder4.build())