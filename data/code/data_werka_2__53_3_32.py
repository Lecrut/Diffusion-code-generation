import math

class Square:
    def __init__(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.area = area

    def find_side_length(self):
        return math.sqrt(self.area)

if __name__ == '__main__':
    sample_area1 = 64.0
    square1 = Square(sample_area1)
    print(square1.find_side_length())

    sample_area2 = 81.0
    square2 = Square(sample_area2)
    print(square2.find_side_length())