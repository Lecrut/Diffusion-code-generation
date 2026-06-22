from functools import cached_property

class RectangularPrism:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    @cached_property
    def surface_area(self):
        return 2 * (self.width * self.height + self.width * self.depth + self.height * self.depth)

    @cached_property
    def volume(self):
        return self.width * self.height * self.depth

if __name__ == '__main__':
    prism = RectangularPrism(5, 10, 15)
    print(prism.surface_area)
    print(prism.volume)