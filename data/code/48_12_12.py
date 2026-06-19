import math

class Square:
    def __init__(self, area):
        self.area = area
        self.side_length = math.sqrt(area)
    
    def calculate_perimeter(self):
        return 4 * self.side_length
    
    def get_side_length(self):
        return self.side_length

if __name__ == '__main__':
    square_area = 16
    square = Square(square_area)
    print(f"Side Length: {square.get_side_length()}")
    print(f"Perimeter: {square.calculate_perimeter()}")