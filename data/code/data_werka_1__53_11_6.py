import math

class Square:
    DEFAULT_AREA = 16.0
    
    def __init__(self, area=None):
        if area is None:
            self._area = self.DEFAULT_AREA
        else:
            self._area = area
    
    @property
    def side_length(self):
        return self.compute_side_length()
    
    def compute_side_length(self):
        return math.sqrt(self._area)

if __name__ == '__main__':
    sample_area = 25.0
    square_with_custom_area = Square(area=sample_area)
    print(square_with_custom_area.side_length)
    
    default_square = Square()
    print(default_square.side_length)