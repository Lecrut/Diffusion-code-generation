class DiamondRenderer:
    def __init__(self, radius):
        self.radius = radius

    def render(self):
        lines = []
        for i in range(-self.radius, self.radius + 1):
            spaces = abs(i)
            stars = 2 * (self.radius - spaces) + 1
            lines.append(' ' * spaces + '* ' * stars)
        return '\n'.join(lines)

if __name__ == '__main__':
    renderer = DiamondRenderer(4)
    print(renderer.render())