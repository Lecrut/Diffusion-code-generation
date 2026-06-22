class RectangularPrism:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self._surface_area = None

    @property
    def surface_area(self):
        if self._surface_area is None:
            self._surface_area = 2 * (
                self.length * self.width +
                self.width * self.height +
                self.height * self.length
            )
        return self._surface_area

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        if name in ('length', 'width', 'height'):
            super().__setattr__('_surface_area', None)

if __name__ == '__main__':
    prism = RectangularPrism(3.0, 4.0, 5.0)
    print(prism.surface_area)
    prism.length = 6.0
    print(prism.surface_area)