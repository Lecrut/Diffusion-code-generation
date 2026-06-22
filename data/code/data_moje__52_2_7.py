class DiamondPatternRenderer:
    def __init__(self, radius):
        self.radius = radius

    def render(self):
        lines = []
        for i in range(-self.radius, self.radius + 1):
            abs_i = abs(i)
            spaces = self.radius - abs_i
            stars = 2 * abs_i + 1
            line = ' ' * spaces + '* ' * stars
            lines.append(line.rstrip())
        return '\n'.join(lines)

if __name__ == '__main__':
    renderer = DiamondPatternRenderer(4)
    print(renderer.render())