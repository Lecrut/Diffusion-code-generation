from functools import lru_cache

class RectangularPrism:
    def __init__(self, length, width, height):
        self.length = float(length)
        self.width = float(width)
        self.height = float(height)
        self._cached_surface_area = None

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value <= 0:
            raise ValueError("Length must be positive")
        self._length = value
        self._invalidate_cache()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
        self._invalidate_cache()

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value
        self._invalidate_cache()

    @property
    def surface_area(self):
        if self._cached_surface_area is None:
            self._cached_surface_area = self._calculate_surface_area()
        return self._cached_surface_area

    def _calculate_surface_area(self):
        return 2 * (
            self._length * self._width +
            self._width * self._height +
            self._height * self._length
        )

    def _invalidate_cache(self):
        self._cached_surface_area = None

if __name__ == '__main__':
    prism = RectangularPrism(3, 4, 5)
    print(prism.surface_area)

    prism2 = RectangularPrism(10, 10, 10)
    print(prism2.surface_area)

    prism3 = RectangularPrism(1, 2, 3)
    print(prism3.surface_area)
    prism3.length = 5
    print(prism3.surface_area)