class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    square_dimensions = {'side_length': 6}
    square = Square(square_dimensions['side_length'])
    print(f"The area of the square with side length {square_dimensions['side_length']} is: {square.area()}")