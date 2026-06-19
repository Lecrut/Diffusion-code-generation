class Square:

    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError('Side length must be positive')
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2
if __name__ == '__main__':
    test_cases = [5, 10, -3, 0]
    for value in test_cases:
        try:
            square = Square(value)
            print(f'Square with side length {value} has an area of {square.area()}')
        except ValueError as e:
            print(f'Error creating square with side {value}: {e}')