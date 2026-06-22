class CheckerboardGenerator:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def generate(self):
        board = []
        for r in range(self.rows):
            row_data = []
            for c in range(self.cols):
                if (r + c) % 2 == 0:
                    row_data.append(' ' if r % 2 == 0 else 'X')
                else:
                    row_data.append('X' if r % 2 == 0 else ' ')
            board.append(row_data)
        return board

    def to_string(self):
        return '\n'.join([''.join(row) for row in self.generate()])

if __name__ == '__main__':
    generator = CheckerboardGenerator(5, 5)
    print(generator.to_string())