import math

class Square:
    def __init__(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.area = area

    @property
    def side_length(self):
        return math.sqrt(self.area)

if __name__ == '__main__':
    sample_areas = [16, 25, 81]
    for area in sample_areas:
        square = Square(area)
        print(square.side_length)