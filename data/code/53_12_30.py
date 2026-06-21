import math

def validate_area(area):
    if area < 0:
        raise ValueError("Area cannot be negative")

def calculate_square_side_length(area):
    validate_area(area)
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
        print(square.side_length())
    except ValueError as e:
        print(e)