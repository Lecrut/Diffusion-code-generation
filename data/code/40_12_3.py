class RectangularPrism:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    @property
    def surface_area(self):
        if not hasattr(self, '_surface_area'):
            self._surface_area = 2 * (self.length * self.width + self.length * self.height + self.width * self.height)
        return self._surface_area

if __name__ == '__main__':
    prism = RectangularPrism(2, 3, 4)
    print(prism.surface_area)