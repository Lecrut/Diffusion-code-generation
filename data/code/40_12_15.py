import functools

class RectangularPrism:
    def __init__(self, length, width, height):
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive numbers")
        self.length = length
        self.width = width
        self.height = height
        self._surface_area = None

    @property
    def surface_area(self):
        if self._surface_area is not None:
            return self._surface_area
        l = self.length
        w = self.width
        h = self.height
        self._surface_area = 2 * (l * w + l * h + w * h)
        return self._surface_area

    def volume(self):
        return self.length * self.width * self.height

if __name__ == '__main__':
    prism = RectangularPrism(3.0, 4.0, 5.0)
    area = prism.surface_area
    print(area)
    vol = prism.volume()
    print(vol)