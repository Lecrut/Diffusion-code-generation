import math

class Square:
    DEFAULT_AREA = 16.0
    
    def __init__(self, area=DEFAULT_AREA):
        self._area = area
    
    @property
    def side_length(self):
        return self._compute_side_length()
    
    def _compute_side_length(self):
        return math.sqrt(self._area)

if __name__ == '__main__':
    square = Square()
    print(square.side_length)