class DiamondRenderer:
    def __init__(self):
        self.radius = 4

    def render(self):
        r = self.radius
        lines = []
        for i in range(1, r + 1):
            spaces = ' ' * (r - i)
            stars = '*' * (2 * i - 1)
            lines.append(spaces + stars)
        for i in range(r - 1, 0, -1):
            spaces = ' ' * (r - i)
            stars = '*' * (2 * i - 1)
            lines.append(spaces + stars)
        return '\n'.join(lines)

if __name__ == '__main__':
    renderer = DiamondRenderer()
    print(renderer.render())