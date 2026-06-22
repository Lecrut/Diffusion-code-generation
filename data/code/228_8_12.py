class TrianglePattern:
    def __init__(self, height):
        self.height = height

    @staticmethod
    def generate_row(i):
        return ' '.join(str(j) for j in range(1, i + 1))

    def triangle_generator(self):
        for i in range(1, self.height + 1):
            yield self.generate_row(i)

if __name__ == '__main__':
    pattern = TrianglePattern(5)
    for row in pattern.triangle_generator():
        print(row)