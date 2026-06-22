class TriangleDrawer:
    def __init__(self, height):
        self.height = height

    @staticmethod
    def calculate_width(height):
        return 2 * height - 1

    def draw_triangle(self):
        width = self.calculate_width(self.height)
        for i in range(1, self.height + 1):
            spaces = ' ' * (width // 2 - i + 1)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)

if __name__ == '__main__':
    drawer = TriangleDrawer(5)
    drawer.draw_triangle()