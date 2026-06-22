class Square:
    def __init__(self, side_length):
        self.set_side_length(side_length)

    def set_side_length(self, side_length):
        if side_length <= 0:
            raise ValueError('Side length must be positive')
        self._side_length = side_length

    def area(self):
        return self._side_length ** 2

if __name__ == '__main__':
    try:
        square1 = Square(6)
        print(square1.area())
        square2 = Square(-5)
        print(square2.area())
    except ValueError as e:
        print(e)