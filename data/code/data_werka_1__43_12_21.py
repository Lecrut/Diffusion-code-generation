class Square:

    def __init__(self, side_length: float):
        if side_length <= 0:
            raise ValueError('Side length must be positive')
        self.side_length = side_length

    def get_area(self) -> float:
        return self.side_length * self.side_length
if __name__ == '__main__':
    try:
        square1 = Square(7.5)
        area1 = square1.get_area()
        print(f'Area of square 1: {area1}')
        square2 = Square(-3)
        area2 = square2.get_area()
        print(f'Area of square 2: {area2}')
    except ValueError as e:
        print(e)