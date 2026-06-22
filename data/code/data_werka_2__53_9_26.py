import math

class Square:
    INITIAL_AREA = 16.0
    
    def __init__(self, area=INITIAL_AREA):
        if area <= 0:
            raise ValueError("Area must be positive")
        self._area = area
    
    @property
    def side_length(self):
        return self._calculate_side()
    
    def _calculate_side(self):
        return math.sqrt(self._area)

if __name__ == '__main__':
    try:
        default_square = Square()
        print(f"Default square side length: {default_square.side_length}")
        
        custom_square = Square(area=49.0)
        print(f"Custom square with area 49.0 side length: {custom_square.side_length}")
        
        invalid_square = Square(area=-16.0)
    except ValueError as e:
        print(e)