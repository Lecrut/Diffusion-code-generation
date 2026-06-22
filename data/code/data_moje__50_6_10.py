class StarTriangleGenerator:
    def __init__(self, height):
        if not isinstance(height, int) or height <= 0:
            raise ValueError("Height must be a positive integer")
        self.height = height

    def generate(self):
        max_width = 2 * self.height - 1
        upper = ['*' * (2 * i - 1).center(max_width) for i in range(1, self.height + 1)]
        lower = ['*' * (2 * i - 1).center(max_width) for i in range(self.height - 1, 0, -1)]
        return '\n'.join(upper + lower)

if __name__ == '__main__':
    generator = StarTriangleGenerator(6)
    print(generator.generate())