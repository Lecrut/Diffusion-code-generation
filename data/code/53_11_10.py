import math

class Square:
    _DEFAULT_AREA = 16.0
    
    def __init__(self, area=None):
        if area is None:
            self._area = self._DEFAULT_AREA
        else:
            self._area = area
    
    @property
    def side_length(self):
        return self._calculate_side_length()
    
    def _calculate_side_length(self):
        return math.sqrt(self._area)

if __name__ == '__main__':
    custom_area_value = 9.0
    square_with_custom_area = Square(area=custom_area_value)
    print("Side length with custom area:", square_with_custom_area.side_length)
    
    default_square = Square()
    print("Default side length:", default_square.side_length)