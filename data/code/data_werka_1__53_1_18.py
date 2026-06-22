class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    @staticmethod
    def calculate_area(side_length):
        return side_length * side_length

    def area(self):
        return Square.calculate_area(self.side_length)

if __name__ == '__main__':
    side_value = 7
    square = Square(side_value)
    print(square.area())