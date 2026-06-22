import functools

class RectangularPrism:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    @functools.cached_property
    def surface_area(self):
        return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)

    @functools.cached_property
    def volume(self):
        return self.length * self.width * self.height

if __name__ == '__main__':
    prism = RectangularPrism(5, 10, 3)
    print(prism.surface_area)
    print(prism.volume)