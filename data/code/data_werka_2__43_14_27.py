class Square:

    def __init__(self, side_length):
        if not isinstance(side_length, (int, float)):
            raise ValueError('Side length must be a numeric value.')
        if side_length < 0:
            raise ValueError('Side length cannot be negative.')
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * self.side_length
if __name__ == '__main__':
    try:
        square1 = Square(5)
        print(f'Area of square with side 5: {square1.calculate_area()}')
        square2 = Square(3.5)
        print(f'Area of square with side 3.5: {square2.calculate_area()}')
        square3 = Square(-2)
    except ValueError as e:
        print(e)
    try:
        square4 = Square('a')
    except ValueError as e:
        print(e)