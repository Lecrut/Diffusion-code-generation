import math

class Square:
    DEFAULT_AREA = 16.0
    
    def __init__(self):
        self._area = self.DEFAULT_AREA
    
    @property
    def side_length(self):
        return self._calculate_side_length()
    
    def _calculate_side_length(self):
        return math.sqrt(self._area)

if __name__ == '__main__':
    default_square = Square()
    print(default_square.side_length)