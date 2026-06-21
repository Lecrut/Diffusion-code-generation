import math

class Square:
    DEFAULT_AREA = 16.0
    
    def __init__(self, area=DEFAULT_AREA):
        self._area = area
        if self._area <= 0:
            raise ValueError("Area must be positive")
    
    @property
    def side_length(self):
        return self._calculate_side_length()
    
    def _calculate_side_length(self):
        return math.sqrt(self._area)

if __name__ == '__main__':
    try:
        square1 = Square(area=9.0)
        print(f"Side length for area 9.0: {square1.side_length}")
        
        square2 = Square()
        print(f"Side length for default area: {square2.side_length}")
        
        invalid_square = Square(area=-4.0)
    except ValueError as e:
        print(e)