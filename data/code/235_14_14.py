class ZigzagGenerator:
    TOP_HALF = 1
    BOTTOM_HALF = 2

    @staticmethod
    def generate_line(width, orientation):
        line = [' ' * width]
        for i in range(width // 2):
            if orientation == ZigzagGenerator.TOP_HALF:
                line[i] = '*' * (i + 1)
                line[-(i + 1)] = '*' * (i + 1)
            else:
                line[i] = ' ' * (width - i - 1) + '*' * (i + 1)
                line[-(i + 1)] = ' ' * (i - i) + '*' * (i + 1)
        return ''.join(line)

    @staticmethod
    def generate_pattern(width, height):
        pattern = []
        for y in range(height):
            orientation = ZigzagGenerator.TOP_HALF if y % 2 == 0 else ZigzagGenerator.BOTTOM_HALF
            line = ZigzagGenerator.generate_line(width, orientation)
            pattern.extend([line] * (width // 2))
        return '\n'.join(pattern)

if __name__ == '__main__':
    print(ZigzagGenerator.generate_pattern(5, 3))