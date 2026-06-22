class DiamondRenderer:
    def __init__(self, radius=4):
        self.radius = radius

    def render(self):
        lines = []
        for i in range(-self.radius, self.radius + 1):
            space_count = abs(i)
            star_count = 2 * (self.radius - abs(i)) + 1
            line = ' ' * space_count + '*' * star_count
            lines.append(line)
        return '\n'.join(lines)

if __name__ == '__main__':
    renderer = DiamondRenderer()
    print(renderer.render())