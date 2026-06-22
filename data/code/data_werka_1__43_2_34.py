class Square:

    def __init__(self, side_length):
        if not isinstance(side_length, (int, float)):
            raise ValueError('Side length must be a numeric value.')
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * self.side_length
if __name__ == '__main__':
    try:
        square1 = Square(4)
        print(f'Area of square with side 4: {square1.calculate_area()}')
        square2 = Square(8.5)
        print(f'Area of square with side 8.5: {square2.calculate_area()}')
        square3 = Square('a')
        print(f"Area of square with side 'a': {square3.calculate_area()}")
    except ValueError as e:
        print(e)