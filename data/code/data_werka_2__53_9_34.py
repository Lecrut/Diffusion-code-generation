import math

class Square:
    DEFAULT_AREA = 16.0
    
    def __init__(self, area=DEFAULT_AREA):
        if area <= 0:
            raise ValueError("Area must be positive")
        self._area = area
    
    @property
    def side_length(self):
        return self._calculate_side_length()
    
    def _calculate_side_length(self):
        length = math.sqrt(self._area)
        return length

if __name__ == '__main__':
    try:
        square = Square(area=20.0)
        print(f"Side length for area 20.0: {square.side_length}")
        
        default_square = Square()
        print(f"Side length for default area: {default_square.side_length}")
        
        invalid_square = Square(area=-5.0)
    except ValueError as e:
        print(e)