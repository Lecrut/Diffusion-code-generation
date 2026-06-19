import math

class Square:
    DEFAULT_AREA = 16.0

    def __init__(self, area=None):
        if area is not None and area <= 0:
            raise ValueError('Area must be positive')
        self._area = area if area is not None else self.DEFAULT_AREA

    @property
    def side_length(self):
        return self._compute_side_length()

    def _compute_side_length(self):
        return math.sqrt(self._area)
if __name__ == '__main__':
    try:
        default_square = Square()
        print(default_square.side_length)
        custom_area_square = Square(area=25.0)
        print(custom_area_square.side_length)
        invalid_square = Square(area=-4.0)
    except ValueError as e:
        print(e)