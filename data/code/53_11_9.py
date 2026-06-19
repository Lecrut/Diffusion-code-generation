import math

class Square:
    FIXED_AREA = 16.0
    
    def __init__(self):
        self._area = Square.FIXED_AREA
    
    @property
    def side_length(self):
        return self._compute_side_length()
    
    def _compute_side_length(self):
        return math.sqrt(self._area)

if __name__ == '__main__':
    sample_square = Square()
    print(sample_square.side_length)