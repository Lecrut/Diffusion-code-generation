import math

class Square:
    AREA_CONSTANT = 16.0
    
    def __init__(self, area=None):
        if area is None:
            self._area = self.AREA_CONSTANT
        else:
            self._area = area
    
    @property
    def side_length(self):
        return self.calculate_side_length()
    
    def calculate_side_length(self):
        return math.sqrt(self._area)

if __name__ == '__main__':
    sample_area = 36.0
    custom_square = Square(area=sample_area)
    print(custom_square.side_length)
    default_square = Square()
    print(default_square.side_length)