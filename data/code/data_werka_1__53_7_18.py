class Square:

    def __init__(self, side_length):
        if not isinstance(side_length, (int, float)):
            raise ValueError('Side length must be an integer or float.')
        if side_length < 0:
            raise ValueError('Side length cannot be negative.')
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length
if __name__ == '__main__':
    square1 = Square(5)
    print(square1.area())
    square2 = Square(0)
    print(square2.area())
    square3 = Square(3.5)
    print(square3.area())