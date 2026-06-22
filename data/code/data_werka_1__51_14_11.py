class Square:
    def __init__(self, side_length):
        if not isinstance(side_length, (int, float)) or side_length <= 0:
            raise ValueError("Side length must be a positive number")
        self.side_length = side_length

    def perimeter(self):
        return 4 * self.side_length

if __name__ == '__main__':
    try:
        square = Square(8.5)
        print(square.perimeter())
    except ValueError as e:
        print(e)