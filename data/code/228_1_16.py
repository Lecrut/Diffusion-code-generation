class TriangleGenerator:
    def generate(self, height):
        return [[1] * (i + 1) for i in range(height)]

if __name__ == '__main__':
    generator = TriangleGenerator()
    triangle = generator.generate(5)
    print(triangle)