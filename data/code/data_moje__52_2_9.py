class DiamondPatternRenderer:
    def __init__(self, radius=4):
        self.radius = radius

    def render(self):
        lines = []
        for i in range(-self.radius + 1, self.radius):
            space_count = abs(i)
            star_count = self.radius - space_count
            line = ' ' * space_count + '*' * (2 * star_count - 1) + ' ' * space_count
            lines.append(line)
        return '\n'.join(lines)

if __name__ == '__main__':
    renderer = DiamondPatternRenderer()
    print(renderer.render())