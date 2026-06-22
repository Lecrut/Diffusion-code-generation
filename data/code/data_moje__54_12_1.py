class HollowSquare:
    def __init__(self, size, char='*', delimiter=' '):
        if size < 1:
            raise ValueError("Size must be at least 1")
        self.size = size
        self.char = char
        self.delimiter = delimiter

    def build(self):
        def row_generator():
            for i in range(self.size):
                if self.size == 1:
                    yield self.char
                elif i == 0 or i == self.size - 1:
                    yield self.delimiter.join([self.char] * self.size)
                else:
                    inner = [self.char] + [self.delimiter] * (self.size - 2) + [self.char]
                    yield self.delimiter.join(inner)

        return '\n'.join(row_generator())

if __name__ == '__main__':
    square1 = HollowSquare(5, '*', ' ')
    print(square1.build())

    square2 = HollowSquare(3, '#', '-')
    print(square2.build())

    square3 = HollowSquare(1, 'X', '')
    print(square3.build())