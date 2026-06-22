class TrianglePattern:
    def __init__(self, n):
        self.n = n

    def generate_pattern(self):
        for i in range(1, self.n + 1):
            yield ' '.join(str(j) for j in range(1, i + 1))

if __name__ == '__main__':
    pattern = TrianglePattern(5)
    for row in pattern.generate_pattern():
        print(row)