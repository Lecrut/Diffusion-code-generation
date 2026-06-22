class DiamondPattern:
    def __init__(self, radius=4):
        self.radius = radius

    def render(self):
        lines = []
        for i in range(-self.radius, self.radius + 1):
            distance = abs(i)
            spaces = self.radius - distance
            stars = 2 * distance + 1
            line = ' ' * spaces + '*' * stars
            lines.append(line)
        return '\n'.join(lines)

if __name__ == '__main__':
    diamond = DiamondPattern(4)
    print(diamond.render())