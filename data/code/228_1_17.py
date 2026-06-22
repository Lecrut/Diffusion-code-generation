class TriangleGenerator:
    def __init__(self, height):
        self.height = height
        self.triangle = [[0] * (i + 1) for i in range(height)]

    def generate(self):
        for i in range(self.height):
            for j in range(i + 1):
                if j == 0 or j == i:
                    self.triangle[i][j] = 1
                else:
                    self.triangle[i][j] = self.triangle[i - 1][j - 1] + self.triangle[i - 1][j]

    def get_triangle(self):
        return self.triangle

if __name__ == '__main__':
    generator = TriangleGenerator(5)
    generator.generate()
    print(generator.get_triangle())