class DiamondRenderer:
    @staticmethod
    def render_diamond(n):
        top_half = [f"{' ' * (n - i - 1)}*{'*' * (2 * i + 1)}" for i in range(n)]
        bottom_half = top_half[:-1][::-1]
        diamond_lines = top_half + bottom_half
        for line in diamond_lines:
            print(line)

if __name__ == '__main__':
    renderer = DiamondRenderer()
    renderer.render_diamond(5)