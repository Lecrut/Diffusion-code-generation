class RectangularPrism:
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def surface_area(self):
        return 2 * (self._length * self._width + self._length * self._height + self._width * self._height)

if __name__ == '__main__':
    prism = RectangularPrism(3, 4, 5)
    print(prism.surface_area)