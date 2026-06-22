from functools import cached_property

class RectangularPrism:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    @cached_property
    def surface_area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

    @cached_property
    def volume(self):
        return self.length * self.width * self.height

if __name__ == '__main__':
    prism = RectangularPrism(3, 4, 5)
    print(prism.surface_area)
    print(prism.volume)