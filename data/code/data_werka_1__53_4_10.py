import math

class Square:
    def __init__(self, area):
        self.area = area

    @staticmethod
    def find_side_length(area):
        return math.sqrt(area)

if __name__ == '__main__':
    sample_area = 25.0
    square = Square(sample_area)
    side_length = square.find_side_length(square.area)
    print(side_length)