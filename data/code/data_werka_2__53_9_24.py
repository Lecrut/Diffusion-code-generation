import math

class Square:
    _DEFAULT_AREA = 16.0
    
    def __init__(self, area=_DEFAULT_AREA):
        self._validate_area(area)
        self._area = area
    
    def _validate_area(self, area):
        if area <= 0:
            raise ValueError("Area must be positive")
    
    @property
    def side_length(self):
        return self._compute_side_length()
    
    def _compute_side_length(self):
        return math.sqrt(self._area)

if __name__ == '__main__':
    try:
        default_square = Square()
        print(f"Side length for default area: {default_square.side_length}")
        
        custom_square = Square(area=25.0)
        print(f"Side length for area 25.0: {custom_square.side_length}")
        
        invalid_square = Square(area=-10.0)
    except ValueError as e:
        print(e)