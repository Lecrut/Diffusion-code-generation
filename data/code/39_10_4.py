import math

class Prism:
    def __init__(self, base_area, height):
        if base_area <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self._base_area = base_area
        self._height = height

    @property
    def base_area(self):
        return self._base_area

    @property
    def height(self):
        return self._height

    def compute_volume(self):
        if self._base_area is None or self._height is None:
            return 0.0
        return self._base_area * self._height

if __name__ == '__main__':
    my_prism = Prism(12.5, 8.0)
    print(my_prism.compute_volume())