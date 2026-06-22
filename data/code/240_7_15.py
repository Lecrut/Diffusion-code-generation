class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    @staticmethod
    def calculate_area(side_length):
        return side_length * side_length

if __name__ == '__main__':
    square = Square(12)
    area = Square.calculate_area(square.side_length)
    print(f"The area of a square with side {square.side_length} is: {area}")