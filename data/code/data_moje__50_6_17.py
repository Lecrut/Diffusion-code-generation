class StarTriangleGenerator:
    MAX_HEIGHT = 6

    @staticmethod
    def _build_line(row_index, max_height):
        spaces = ' ' * (max_height - row_index)
        stars = '*' * (2 * row_index - 1)
        return spaces + stars

    @classmethod
    def generate(cls, height):
        lines = []
        for i in range(1, height + 1):
            lines.append(cls._build_line(i, height))
        for i in range(height - 1, 0, -1):
            lines.append(cls._build_line(i, height))
        return '\n'.join(lines)

if __name__ == '__main__':
    generator = StarTriangleGenerator()
    print(generator.generate(generator.MAX_HEIGHT))