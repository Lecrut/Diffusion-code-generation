class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.calculate_area()

    @staticmethod
    def calculate_area(side_length):
        return side_length ** 2

if __name__ == '__main__':
    sample_side_length = 7
    square = Square(sample_side_length)
    print(square.area())