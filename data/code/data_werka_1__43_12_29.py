class Square:

    def __init__(self, side_length: float):
        if side_length <= 0:
            raise ValueError('Side length must be positive')
        self.side_length = side_length

    def get_area(self) -> float:
        return self.side_length * self.side_length
if __name__ == '__main__':
    try:
        square1 = Square(5.0)
        print(f'Area of square 1: {square1.get_area()}')
        square2 = Square(7.2)
        print(f'Area of square 2: {square2.get_area()}')
        invalid_square = Square(-3.0)
    except ValueError as e:
        print(e)