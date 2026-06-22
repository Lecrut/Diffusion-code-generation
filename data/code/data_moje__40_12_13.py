import math

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

    @property
    def volume(self):
        return self.length * self.width * self.height

    @property
    def space_diagonal(self):
        return math.sqrt(
            self.length ** 2 +
            self.width ** 2 +
            self.height ** 2
        )

if __name__ == '__main__':
    prism = RectangularPrism(3.0, 4.0, 5.0)
    print(prism.surface_area)
    print(prism.volume)
    print(prism.space_diagonal)