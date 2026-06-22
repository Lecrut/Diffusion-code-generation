class HollowSquare:
    def __init__(self, size, char='*', delimiter=' '):
        if size < 1:
            raise ValueError("Size must be at least 1")
        if not isinstance(char, str) or len(char) != 1:
            raise ValueError("Char must be a single character")
        if not isinstance(delimiter, str) or len(delimiter) != 1:
            raise ValueError("Delimiter must be a single character")
        self.size = size
        self.char = char
        self.delimiter = delimiter

    def build(self):
        row_gen = (
            self.delimiter.join(
                self.char if i == 0 or i == self.size - 1 or j == 0 or j == self.size - 1 else self.delimiter
                for j in range(self.size)
            )
            for i in range(self.size)
        )
        return '\n'.join(row_gen)

if __name__ == '__main__':
    square = HollowSquare(5, '#', '-')
    result = square.build()
    print(result)