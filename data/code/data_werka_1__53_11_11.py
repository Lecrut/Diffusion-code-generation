import math

class Square:
    DEFAULT_AREA = 16.0

    def __init__(self, area=None):
        self._area = area if area is not None else self.DEFAULT_AREA

    @property
    def side_length(self):
        return self._calculate_side()

    def _calculate_side(self):
        return math.sqrt(self._area)

if __name__ == '__main__':
    sample_area = 20.0
    square_with_custom_area = Square(area=sample_area)
    print(square_with_custom_area.side_length)
    
    default_square = Square()
    print(default_square.side_length)