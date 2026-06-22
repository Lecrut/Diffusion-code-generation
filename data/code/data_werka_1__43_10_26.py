class Square:

    def __init__(self, side_length):
        if not isinstance(side_length, (int, float)) or side_length <= 0:
            raise ValueError('Side length must be a positive number.')
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2
if __name__ == '__main__':
    try:
        square1 = Square(5)
        print(f'Square with side {square1.side_length} has an area of {square1.area()}')
        square2 = Square(7.2)
        print(f'Square with side {square2.side_length} has an area of {square2.area()}')
        invalid_square = Square(-3)
    except ValueError as e:
        print(e)