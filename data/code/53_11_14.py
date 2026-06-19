import math

class Square:
    FIXED_AREA = 16.0
    
    def __init__(self):
        self._area = self.FIXED_AREA
    
    @property
    def side_length(self):
        return self.calculate_side_length()
    
    def calculate_side_length(self):
        return math.sqrt(self._area)

if __name__ == '__main__':
    default_square = Square()
    print("Side length of the square with fixed area:", default_square.side_length)
    
    custom_area = 25.0
    custom_square = Square()
    custom_square._area = custom_area
    print("Side length of the square with custom area:", custom_square.side_length)