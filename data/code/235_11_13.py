class DiamondRenderer:
    def __init__(self):
        self.diamond_lines = [
            "   *",
            "  ***",
            " *****",
            "*******",
            " *****",
            "  ***",
            "   *"
        ]

    def render_diamond(self):
        for line in self.diamond_lines:
            print(line)

if __name__ == '__main__':
    renderer = DiamondRenderer()
    renderer.render_diamond()