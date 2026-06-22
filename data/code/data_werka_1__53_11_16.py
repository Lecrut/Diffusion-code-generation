import math

class Square:
    AREA = 16.0
    
    def __init__(self):
        self._area = self.AREA
    
    @property
    def side_length(self):
        return self._compute_side_length()
    
    @staticmethod
    def _compute_side_length(area):
        return math.sqrt(area)

if __name__ == '__main__':
    default_square = Square()
    print(default_square.side_length)