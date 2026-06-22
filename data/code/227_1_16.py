class StarPatternGenerator:
    @staticmethod
    def generate_pattern(n):
        pattern = []
        for i in range(n):
            spaces = " " * (n - 1 - i)
            stars = "*" * (2 * n - 1 - 2 * i)
            pattern.append(spaces + stars)
        return pattern

if __name__ == '__main__':
    pattern = StarPatternGenerator.generate_pattern(4)
    for line in pattern:
        print(line)