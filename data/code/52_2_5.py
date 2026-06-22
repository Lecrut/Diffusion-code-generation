class DiamondRenderer:
    def __init__(self, radius):
        self.radius = radius

    def render(self):
        lines = []
        for i in range(1, self.radius + 1):
            spaces = ' ' * (self.radius - i)
            stars = '* ' * i
            lines.append(spaces + stars.strip())
        for i in range(self.radius - 1, 0, -1):
            spaces = ' ' * (self.radius - i)
            stars = '* ' * i
            lines.append(spaces + stars.strip())
        return '\n'.join(lines)

if __name__ == '__main__':
    renderer = DiamondRenderer(4)
    print(renderer.render())