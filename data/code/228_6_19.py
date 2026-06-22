class TriangleBuilder:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def build_pyramid(self, row=0, spaces=0):
        if row == self.height:
            return
        print(' ' * spaces + '*' * (2 * row + 1))
        self.build_pyramid(row + 1, spaces + 1)

if __name__ == '__main__':
    builder = TriangleBuilder(5, 4)
    builder.build_pyramid()