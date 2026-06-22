class DiamondRenderer:
    def __init__(self):
        self.radius = 4

    def render(self):
        lines = []
        for i in range(-self.radius, self.radius + 1):
            spaces = abs(i)
            stars = self.radius - abs(i) + 1
            line = " " * spaces + "* " * (2 * stars - 1)
            lines.append(line.rstrip())
        return "\n".join(lines)

if __name__ == '__main__':
    renderer = DiamondRenderer()
    result = renderer.render()
    print(result)