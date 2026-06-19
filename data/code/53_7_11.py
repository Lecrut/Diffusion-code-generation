class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    sample_side_length = 7
    square = Square(sample_side_length)
    print(square.calculate_area())