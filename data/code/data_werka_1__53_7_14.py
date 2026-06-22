class Square:

    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * self.side_length
if __name__ == '__main__':
    square1 = Square(5)
    print('Area of square with side length 5:', square1.calculate_area())
    square2 = Square(0)
    print('Area of square with side length 0:', square2.calculate_area())
    square3 = Square(7.5)
    print('Area of square with side length 7.5:', square3.calculate_area())