class DiamondRenderer:
    def __init__(self, radius=4):
        self.radius = radius

    def render(self):
        result = []
        for i in range(-self.radius, self.radius + 1):
            spaces = abs(i)
            stars = self.radius - spaces
            line = " " * spaces + "*" * (2 * stars + 1)
            result.append(line)
        return "\n".join(result)

if __name__ == "__main__":
    renderer = DiamondRenderer(4)
    print(renderer.render())