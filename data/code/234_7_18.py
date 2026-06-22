class CheckerboardGenerator:
    def __init__(self, size):
        self.size = size

    def generate_row(self, row_number):
        return [(row_number + col) % 2 for col in range(self.size)]

    def __iter__(self):
        row_number = 0
        while True:
            yield self.generate_row(row_number)
            row_number += 1

if __name__ == '__main__':
    checkerboard_gen = CheckerboardGenerator(8)
    print("First 4 rows:")
    for _ in range(4):
        print(next(checkerboard_gen))
    print("\nNext 4 rows:")
    for _ in range(4):
        print(next(checkerboard_gen))