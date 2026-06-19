import math

class Square:
    def __init__(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.area = area

    def side_length(self):
        return math.sqrt(self.area)

    def perimeter(self):
        return 4 * self.side_length()

if __name__ == '__main__':
    square_area = 16
    try:
        square = Square(square_area)
        print("Side Length:", square.side_length())
        print("Perimeter:", square.perimeter())
    except ValueError as e:
        print(e)