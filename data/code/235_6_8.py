class PyramidGenerator:
    MAX_LEVELS = 5

    @staticmethod
    def generate_line(level):
        return " " * (PyramidGenerator.MAX_LEVELS - level) + "+" * (2 * level - 1)

    def generate_pyramid(self):
        for i in range(1, self.MAX_LEVELS + 1):
            yield self.generate_line(i)

if __name__ == '__main__':
    pyramid = PyramidGenerator()
    for line in pyramid.generate_pyramid():
        print(line)