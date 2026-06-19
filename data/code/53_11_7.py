import math

class Square:
    _AREA = 16.0
    
    @property
    def side_length(self):
        return self._compute_side_length()
    
    def _compute_side_length(self):
        return math.sqrt(self._AREA)

if __name__ == '__main__':
    square = Square()
    print(square.side_length)