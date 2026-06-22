class Square:

    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2
if __name__ == '__main__':
    square = Square(5)
    print(square.calculate_area())
    print(square.calculate_area())