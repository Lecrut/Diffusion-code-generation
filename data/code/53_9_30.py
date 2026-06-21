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
        side = math.sqrt(self._area)
        return side

if __name__ == '__main__':
    default_square = Square()
    print(f"Side length for default square: {default_square.side_length}")
    
    custom_square = Square(area=49.0)
    print(f"Side length for square with area 49.0: {custom_square.side_length}")