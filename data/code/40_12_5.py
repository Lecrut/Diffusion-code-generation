class RectangularPrism:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    @property
    def surface_area(self):
        return 2 * (self.length * self.width + self.width * self.height + self.length * self.height)

if __name__ == '__main__':
    p = RectangularPrism(3, 4, 5)
    print(p.surface_area)