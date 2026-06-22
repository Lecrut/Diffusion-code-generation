class StarTriangleRenderer:
    def __init__(self, height, symbol="*"):
        self.height = height
        self.symbol = symbol

    def get_lines(self):
        lines = []
        for i in range(1, self.height + 1):
            lines.append(self.symbol * i)
        return lines

    def render(self):
        lines = self.get_lines()
        for line in lines:
            print(line)
        return "\n".join(lines)

if __name__ == '__main__':
    renderer = StarTriangleRenderer(6, "*")
    result = renderer.render()
    print(result)