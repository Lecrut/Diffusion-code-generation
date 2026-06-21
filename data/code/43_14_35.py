class Square:
    MIN_SIDE_LENGTH = 0

    def __init__(self, side_length):
        self.side_length = side_length

    @property
    def side_length(self):
        return self._side_length

    @side_length.setter
    def side_length(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Side length must be a numeric value.')
        if value < Square.MIN_SIDE_LENGTH:
            raise ValueError('Side length cannot be negative.')
        self._side_length = value

    def calculate_area(self):
        return self.side_length * self.side_length
if __name__ == '__main__':
    try:
        square1 = Square(5)
        print(f'Area of square with side {square1.side_length}: {square1.calculate_area()}')
        square2 = Square(3.5)
        print(f'Area of square with side {square2.side_length}: {square2.calculate_area()}')
        square3 = Square(-2)
        print(f'Area of square with side {square3.side_length}: {square3.calculate_area()}')
    except ValueError as e:
        print(e)
    try:
        square4 = Square('a')
        print(f'Area of square with side {square4.side_length}: {square4.calculate_area()}')
    except ValueError as e:
        print(e)