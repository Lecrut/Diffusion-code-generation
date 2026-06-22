class DiamondPattern:
    SEPARATOR = '\n'

    @staticmethod
    def generate(size):
        lines = []
        upper = [' ' * (size - i - 1) + '*' * (2 * i + 1) for i in range(size)]
        lower = [' ' * (size - i - 2) + '*' * (2 * i - 1) for i in range(size - 1, 0, -1)]
        lines.extend(upper)
        lines.extend(lower)
        return DiamondPattern.SEPARATOR.join(lines)

if __name__ == '__main__':
    result = DiamondPattern.generate(5)
    print(result)