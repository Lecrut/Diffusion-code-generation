class TriangleGenerator:
    def __init__(self, size):
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Size must be a positive integer")
        self.size = size

    def generate(self):
        triangle = []
        for i in range(1, self.size + 1):
            row = [1] * i
            for j in range(1, i - 1):
                row[j] = triangle[i-2][j-1] + triangle[i-2][j]
            triangle.append(row)
        return triangle

if __name__ == '__main__':
    generator = TriangleGenerator(5)
    print(generator.generate())