class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    sample_square = Square(5)
    print(sample_square.calculate_area())
    sample_rectangle = Square(10)
    print(sample_rectangle.calculate_area())