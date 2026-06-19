class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    @staticmethod
    def calculate_area(side_length):
        return side_length ** 2

    def area(self):
        return Square.calculate_area(self.side_length)

if __name__ == '__main__':
    square = Square(6)
    print(f"The side length is: {square.side_length}")
    print(f"The area of the square is: {square.area()}")