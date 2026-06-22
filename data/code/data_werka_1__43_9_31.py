class Square:
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    try:
        square = Square(5)
        print(f"Area of square with side {square.side_length}: {square.area()}")
    except ValueError as e:
        print(e)