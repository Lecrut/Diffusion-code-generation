import math

class Square:
    FIXED_AREA = 16.0
    
    def __init__(self):
        self._area = self.FIXED_AREA
    
    @property
    def side_length(self):
        return self._calculate_side_length()
    
    def _calculate_side_length(self):
        if self._area <= 0:
            raise ValueError("Area must be positive")
        return math.sqrt(self._area)

if __name__ == '__main__':
    square = Square()
    print(f"Side length for fixed area: {square.side_length}")