class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    square = Square(5)
    print(square.calculate_area())