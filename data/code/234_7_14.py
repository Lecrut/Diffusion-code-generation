class CheckerboardGenerator:
    BLACK = 0
    WHITE = 1

    @staticmethod
    def generate_row(row_index, size):
        return [CheckerboardGenerator.BLACK if (row_index + col) % 2 == 0 else CheckerboardGenerator.WHITE for col in range(size)]

    def __iter__(self):
        self.size = 8
        self.row_index = 0
        return self

    def __next__(self):
        if self.row_index >= self.size:
            raise StopIteration
        row = CheckerboardGenerator.generate_row(self.row_index, self.size)
        self.row_index += 1
        return row
if __name__ == '__main__':
    checkerboard_gen = CheckerboardGenerator()
    for _ in range(5):
        print(next(checkerboard_gen))