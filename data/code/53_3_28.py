import math

def find_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

class Square:
    def __init__(self, area):
        self.area = area
        self.side_length = find_side_length(area)
    
    def get_side_length(self):
        return self.side_length

if __name__ == '__main__':
    sample_area1 = 64.0
    square1 = Square(sample_area1)
    print(square1.get_side_length())

    sample_area2 = 81.0
    square2 = Square(sample_area2)
    print(square2.get_side_length())