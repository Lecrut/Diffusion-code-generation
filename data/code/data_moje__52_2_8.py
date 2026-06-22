class DiamondRenderer:
    def __init__(self):
        self.radius = 4

    def render(self):
        lines = []
        for i in range(-self.radius, self.radius + 1):
            spaces = abs(i)
            stars = (self.radius * 2 + 1) - (2 * spaces)
            lines.append(" " * spaces + "*" * stars)
        return "\n".join(lines)

if __name__ == "__main__":
    renderer = DiamondRenderer()
    print(renderer.render())