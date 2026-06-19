class Square:
    def __init__(self, side_length):
        self.set_side_length(side_length)

    def set_side_length(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self._side_length = side_length

    def perimeter(self):
        return 4 * self._side_length

if __name__ == '__main__':
    try:
        square = Square(9)
        print(square.perimeter())
    except ValueError as e:
        print(e)