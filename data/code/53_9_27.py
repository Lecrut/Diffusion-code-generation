import math

class Square:
    _AREA = 16.0
    
    def __init__(self, area=_AREA):
        if area <= 0:
            raise ValueError("Area must be positive")
        self._area = area
    
    @property
    def side_length(self):
        return self._get_side_length()
    
    def _get_side_length(self):
        return math.sqrt(self._area)

if __name__ == '__main__':
    square = Square()
    print(square.side_length)