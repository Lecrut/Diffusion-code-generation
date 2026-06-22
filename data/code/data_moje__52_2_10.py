class DiamondRenderer:
    def __init__(self, radius=4):
        self.radius = radius

    def render(self):
        lines = []
        for i in range(-self.radius, self.radius + 1):
            spaces = abs(i)
            stars = (self.radius - abs(i)) * 2 + 1
            line = ' ' * spaces + '*' * stars
            lines.append(line)
        return '\n'.join(lines)

if __name__ == '__main__':
    renderer = DiamondRenderer(4)
    print(renderer.render())