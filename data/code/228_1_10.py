class TriangleGenerator:
    def __init__(self, height):
        self.height = height

    @staticmethod
    def generate(height):
        triangle = []
        for i in range(1, height + 1):
            row = ['*'] * i
            triangle.append(row)
        return triangle

if __name__ == '__main__':
    generator = TriangleGenerator(5)
    triangle = generator.generate(generator.height)
    for row in triangle:
        print(' '.join(row))