class Square:
    def __init__(self, side_length):
        self.side_length = side_length
    def calculate_area(self):
        return self.side_length * self.side_length
if __name__ == '__main__':
    square1 = Square(5)
    area1 = square1.calculate_area()
    print(area1)
    square2 = Square(10.5)
    area2 = square2.calculate_area()
    print(area2)