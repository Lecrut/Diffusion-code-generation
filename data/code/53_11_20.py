import math

class Square:
    FIXED_AREA = 16.0
    
    def __init__(self):
        self._area = self.FIXED_AREA
    
    @property
    def side_length(self):
        return self._compute_side_length()
    
    def _compute_side_length(self):
        if self._area < 0:
            raise ValueError("Area cannot be negative")
        return math.sqrt(self._area)

if __name__ == '__main__':
    square = Square()
    print(square.side_length)