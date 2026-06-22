def build_symmetric_star_pattern(height):
    if height <= 0:
        return ''
    top_half = [('*' * (2 * i - 1)) for i in range(1, height + 1)]
    bottom_half = [('*' * (2 * i - 1)) for i in range(height - 1, 0, -1)]
    return '\n'.join(top_half + bottom_half)

class StarTrianglePrinter:
    def __init__(self, height):
        self.height = height

    def render(self):
        if self.height <= 0:
            return ''
        lines = []
        current = 1
        while current <= self.height:
            lines.append('*' * (2 * current - 1))
            current += 1
        current = self.height - 1
        while current > 0:
            lines.append('*' * (2 * current - 1))
            current -= 1
        return '\n'.join(lines)

if __name__ == '__main__':
    pattern_func = build_symmetric_star_pattern(6)
    print(pattern_func)
    printer = StarTrianglePrinter(6)
    print(printer.render())