import math

class Square:
    DEFAULT_AREA = 16.0
    
    def __init__(self, area=None):
        self._area = area if area is not None else self.DEFAULT_AREA
    
    @property
    def side_length(self):
        return self._compute_side_length()
    
    def _compute_side_length(self):
        return math.sqrt(self._area)

if __name__ == '__main__':
    default_square = Square()
    print("Side length of the default square:", default_square.side_length)
    
    custom_area_square = Square(area=25.0)
    print("Side length of the square with custom area:", custom_area_square.side_length)