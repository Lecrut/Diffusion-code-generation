class HollowSquareBuilder:
    def __init__(self, size, corner_char='*', edge_char='*', inner_delimiter=' '):
        self.size = size
        self.corner_char = corner_char
        self.edge_char = edge_char
        self.inner_delimiter = inner_delimiter

    def build(self):
        def row_generator(row_idx):
            if row_idx == 0 or row_idx == self.size - 1:
                yield ''.join(self.corner_char if (col_idx == 0 or col_idx == self.size - 1) else self.edge_char for col_idx in range(self.size))
            else:
                yield ''.join(self.corner_char if (col_idx == 0 or col_idx == self.size - 1) else self.inner_delimiter for col_idx in range(self.size))
        
        return '\n'.join(row_generator(r) for r in range(self.size))

if __name__ == '__main__':
    builder = HollowSquareBuilder(5, '+', '-', ' ')
    result = builder.build()
    print(result)
    
    builder2 = HollowSquareBuilder(4, '#', '=', '.')
    result2 = builder2.build()
    print(result2)