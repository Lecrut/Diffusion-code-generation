import math

class Square:
    _AREAS = {1: 4.0, 2: 8.0, 3: 16.0, 4: 25.0}

    def __init__(self, version=3):
        self._area = self._AREAS.get(version, 16.0)

    @property
    def side_length(self):
        return self._compute_side_length()

    def _compute_side_length(self):
        return math.sqrt(self._area)
if __name__ == '__main__':
    square_v1 = Square(1)
    print(square_v1.side_length)
    default_square = Square()
    print(default_square.side_length)
    square_v4 = Square(4)
    print(square_v4.side_length)