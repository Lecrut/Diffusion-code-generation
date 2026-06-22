class PyramidGenerator:
    def __init__(self, levels):
        self.levels = levels

    def generate_pyramid(self):
        for i in range(1, self.levels + 1):
            spaces = ' ' * (self.levels - i)
            stars = '*' * (2 * i - 1)
            yield spaces + stars

if __name__ == '__main__':
    pyramid_gen = PyramidGenerator(5)
    for line in pyramid_gen.generate_pyramid():
        print(line)