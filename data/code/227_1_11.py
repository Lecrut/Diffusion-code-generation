class StarPyramid:
    def generate_pattern(self, n):
        pattern = []
        for i in range(n):
            spaces = " " * (n - 1 - i)
            stars = "*" * (2 * n - 1 - 2 * i)
            pattern.append(spaces + stars)
        return pattern

if __name__ == '__main__':
    pyramid = StarPyramid()
    height = 4
    pattern = pyramid.generate_pattern(height)
    for line in pattern:
        print(line)