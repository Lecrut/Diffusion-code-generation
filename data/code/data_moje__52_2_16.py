class DiamondPattern:
    def __init__(self, radius=4):
        self.radius = radius

    def render(self):
        lines = []
        r = self.radius
        for i in range(-r, r + 1):
            abs_i = abs(i)
            spaces = ' ' * (r - abs_i)
            stars = '* ' * (abs_i + 1)
            lines.append(spaces + stars.strip())
        return '\n'.join(lines)

if __name__ == '__main__':
    diamond = DiamondPattern(4)
    print(diamond.render())