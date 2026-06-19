import math

class Square:
    FIXED_AREA = 16.0
    
    def __init__(self):
        self._area = self.FIXED_AREA
    
    @property
    def side_length(self):
        return self._calculate_side_length()
    
    def _calculate_side_length(self):
        return math.sqrt(self._area)

if __name__ == '__main__':
    square_instance = Square()
    print(square_instance.side_length)