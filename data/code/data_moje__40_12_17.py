import math

class RectangularPrism:
    def __init__(self, length, width, height):
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self.length = length
        self.width = width
        self.height = height
        self._surface_area_cache = None
        self._volume_cache = None

    @property
    def surface_area(self):
        if self._surface_area_cache is not None:
            return self._surface_area_cache
        l, w, h = self.length, self.width, self.height
        area = 2 * (l * w + w * h + h * l)
        self._surface_area_cache = area
        return area

    @property
    def volume(self):
        if self._surface_area_cache is not None and self._volume_cache is not None:
            return self._volume_cache
        l, w, h = self.length, self.width, self.height
        vol = l * w * h
        self._volume_cache = vol
        return vol

    def __repr__(self):
        return f"RectangularPrism(length={self.length}, width={self.width}, height={self.height})"

if __name__ == '__main__':
    prism = RectangularPrism(5, 10, 15)
    sa = prism.surface_area
    vol = prism.volume
    print(sa)
    print(vol)