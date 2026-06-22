import math

SQUARE_AREA = 16.0

class Square:
    def __init__(self):
        self._area = SQUARE_AREA
    
    @property
    def side_length(self):
        return self._calculate_side_length()
    
    def _calculate_side_length(self):
        return math.sqrt(self._area)

if __name__ == '__main__':
    sample_square = Square()
    print(sample_square.side_length)