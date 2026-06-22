import math

class Square:
    def __init__(self, area):
        self.area = area
        self.side_length = self._calculate_side_length()
    
    def _calculate_side_length(self):
        return math.sqrt(self.area)
    
    def calculate_perimeter(self):
        return 4 * self.side_length
    
    def get_side_length(self):
        return self.side_length

if __name__ == '__main__':
    square = Square(16)
    print("Side Length:", square.get_side_length())
    print("Perimeter:", square.calculate_perimeter())