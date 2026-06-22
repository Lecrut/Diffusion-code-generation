import math

class Square:
    def __init__(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.area = area

    def calculate_side_length(self):
        return math.sqrt(self.area)

if __name__ == '__main__':
    sample_area1 = 16
    sample_area2 = 25
    sample_area3 = 81

    square1 = Square(sample_area1)
    square2 = Square(sample_area2)
    square3 = Square(sample_area3)

    print(square1.calculate_side_length())
    print(square2.calculate_side_length())
    print(square3.calculate_side_length())