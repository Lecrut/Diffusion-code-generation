class Square:
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be a positive number.")
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    try:
        square1 = Square(5)
        print(f"The area of the square with side 5 is: {square1.area()}")
        square2 = Square(10.5)
        print(f"The area of the square with side 10.5 is: {square2.area()}")
        square3 = Square(-3)
    except ValueError as e:
        print(f"Error for invalid input: {e}")