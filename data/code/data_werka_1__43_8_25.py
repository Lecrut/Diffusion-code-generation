class Square:
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be a positive number.")
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    try:
        square = Square(6)
        print(f"The area of the square with side length {square.side_length} is: {square.area()}")
    except ValueError as e:
        print(e)