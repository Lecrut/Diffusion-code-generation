class DiamondRenderer:
    def __init__(self):
        self.radius = 4

    def render(self):
        result = []
        for i in range(-self.radius, self.radius + 1):
            spaces = abs(i)
            stars = 2 * (self.radius - spaces) + 1
            line = " " * spaces + "*" * stars
            result.append(line)
        return "\n".join(result)

if __name__ == '__main__':
    renderer = DiamondRenderer()
    print(renderer.render())