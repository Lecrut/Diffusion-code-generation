class Square:
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

if __name__ == '__main__':
    square1 = Square(5)
    print(square1.calculate_area())

    square2 = Square(7)
    print(square2.calculate_area())