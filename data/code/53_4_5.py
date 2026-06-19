import math

class Square:
    def __init__(self, area):
        self.area = area

    def find_side_length(self):
        return math.sqrt(self.area)

if __name__ == '__main__':
    sample_areas = [16.0, 25.0, 36.0, 49.0]
    for area in sample_areas:
        square = Square(area)
        side_length = square.find_side_length()
        print(f'Area: {area}, Side Length: {side_length}')