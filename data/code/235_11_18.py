class DiamondRenderer:
    DIAMOND_LINES = [
        "   *",
        "  ***",
        " *****",
        "*******",
        " *****",
        "  ***",
        "   *"
    ]

    @staticmethod
    def render_diamond():
        for line in DiamondRenderer.DIAMOND_LINES:
            print(line)

if __name__ == '__main__':
    diamond_renderer = DiamondRenderer()
    diamond_renderer.render_diamond()