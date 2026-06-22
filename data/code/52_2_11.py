class DiamondRenderer:
    def __init__(self, radius):
        self.radius = radius

    def render(self):
        lines = []
        for i in range(1, self.radius + 1):
            lines.append(' ' * (self.radius - i) + '*' * (2 * i - 1))
        for i in range(self.radius - 1, 0, -1):
            lines.append(' ' * (self.radius - i) + '*' * (2 * i - 1))
        return '\n'.join(lines)

if __name__ == '__main__':
    renderer = DiamondRenderer(4)
    print(renderer.render())