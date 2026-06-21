class Square:
    def __init__(self, side_length):
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_squares = [
        Square(4),
        Square(6),
        Square(9)
    ]
    for square in sample_squares:
        print(f"The area of a square with side length {square.side_length} is {square.area()}")