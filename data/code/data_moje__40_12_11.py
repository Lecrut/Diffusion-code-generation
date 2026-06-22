class RectangularPrism:
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height
        self._surface_area = None

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
        if self._surface_area is None:
            self._surface_area = 2 * (
                self._length * self._width +
                self._width * self._height +
                self._height * self._length
            )
        return self._surface_area

    def invalidate_cache(self):
        self._surface_area = None

if __name__ == '__main__':
    prism = RectangularPrism(5, 6, 7)
    print(prism.surface_area)
    print(prism.surface_area)
    prism._length = 10
    prism.invalidate_cache()
    print(prism.surface_area)