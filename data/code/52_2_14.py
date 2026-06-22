class DiamondRenderer:
    def __init__(self, radius=4):
        self.radius = radius

    def render_diamond(self):
        lines = []
        for i in range(-self.radius, self.radius + 1):
            spaces = abs(i)
            stars = 2 * (self.radius - abs(i)) + 1
            lines.append(' ' * spaces + '*' * stars)
        return '\n'.join(lines)

if __name__ == '__main__':
    renderer = DiamondRenderer()
    print(renderer.render_diamond())