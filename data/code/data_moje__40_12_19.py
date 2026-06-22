from functools import lru_cache

class RectangularPrism:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    @property
    def surface_area(self):
        return 2 * (
            self.length * self.width +
            self.width * self.height +
            self.height * self.length
        )

    @lru_cache(maxsize=None)
    def cached_surface_area(self):
        return self.surface_area

if __name__ == '__main__':
    prism = RectangularPrism(3.0, 4.0, 5.0)
    print(prism.cached_surface_area())