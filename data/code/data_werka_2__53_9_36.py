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
    
    @staticmethod
    def _calculate_side_length(area):
        return math.sqrt(area)

if __name__ == '__main__':
    try:
        square1 = Square()
        print(f"Side length for default area: {square1.side_length}")
        
        square2 = Square(area=25.0)
        print(f"Side length for area 25.0: {square2.side_length}")
        
        invalid_square = Square(area=-10.0)
    except ValueError as e:
        print(e)