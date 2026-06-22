import math

class Square:
    DEFAULT_AREA = 16.0

    def __init__(self, area=DEFAULT_AREA):
        if area <= 0:
            raise ValueError('Area must be positive')
        self._area = area

    @property
    def side_length(self):
        return self.compute_side_length()

    def compute_side_length(self):
        return math.sqrt(self._area)
if __name__ == '__main__':
    try:
        square_default = Square()
        print(f'Side length for default area: {square_default.side_length}')
        square_custom = Square(area=25.0)
        print(f'Side length for custom area 25.0: {square_custom.side_length}')
        invalid_square = Square(area=-10.0)
    except ValueError as e:
        print(e)