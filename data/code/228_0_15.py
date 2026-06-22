class TriangleDrawer:
    def __init__(self, height):
        self.height = height

    def draw_triangle(self):
        for i in range(1, self.height + 1):
            print(' ' * (self.height - i) + '*' * (2 * i - 1))

if __name__ == '__main__':
    drawer = TriangleDrawer(5)
    drawer.draw_triangle()