class RectangularPrism:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    @property
    def surface_area(self):
        cached_value = getattr(self, '_surface_area', None)
        if cached_value is None:
            result = 2 * (self.length * self.width +
                          self.length * self.height +
                          self.width * self.height)
            self._surface_area = result
            cached_value = result
        return cached_value

    def invalidate_cache(self):
        if hasattr(self, '_surface_area'):
            del self._surface_area

if __name__ == '__main__':
    prism = RectangularPrism(5.0, 3.0, 2.0)
    print(prism.surface_area)