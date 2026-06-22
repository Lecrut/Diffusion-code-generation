class RectangularPrism:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def surface_area(self):
        if self.length <= 0 or self.width <= 0 or self.height <= 0:
            return 0
        l = self.length
        w = self.width
        h = self.height
        return 2 * l * w + 2 * w * h + 2 * h * l

if __name__ == '__main__':
    prism = RectangularPrism(10.5, 4.2, 2.1)
    area = prism.surface_area()
    print(area)