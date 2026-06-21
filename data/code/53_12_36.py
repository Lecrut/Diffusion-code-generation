import math

def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

class Square:
    def __init__(self, area):
        self.area = area
    
    def side_length(self):
        return calculate_square_side_length(self.area)

if __name__ == '__main__':
    sample_area = 49.0
    try:
        square = Square(sample_area)
        side_length = square.side_length()
        print(side_length)
    except ValueError as e:
        print(e)