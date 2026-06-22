class TriangleGenerator:
    def __init__(self, height):
        self.height = height

    def generate_triangle(self):
        for i in range(1, self.height + 1):
            print('*' * i)

if __name__ == '__main__':
    generator = TriangleGenerator(5)
    generator.generate_triangle()