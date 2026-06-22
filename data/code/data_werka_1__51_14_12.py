class Square:
    def __init__(self, side_length):
        self._validate_side_length(side_length)
        self.side_length = side_length

    def _validate_side_length(self, side_length):
        if not isinstance(side_length, (int, float)) or side_length <= 0:
            raise ValueError("Side length must be a positive number")

    def perimeter(self):
        return 4 * self.side_length

    def area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    try:
        square = Square(8)
        print("Perimeter:", square.perimeter())
        print("Area:", square.area())
    except ValueError as e:
        print(e)