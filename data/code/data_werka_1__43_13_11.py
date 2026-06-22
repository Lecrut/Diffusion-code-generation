class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_squares = [Square(3), Square(4), Square(5)]
    for square in sample_squares:
        print(f"The area of the square with side length {square.side_length} is: {square.area()}")