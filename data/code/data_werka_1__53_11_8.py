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
        return self.compute_side_length()
    
    @staticmethod
    def compute_side_length(area):
        return math.sqrt(area)

if __name__ == '__main__':
    default_square = Square()
    print(default_square.side_length)
    
    custom_area_square = Square(25.0)
    print(custom_area_square.side_length)