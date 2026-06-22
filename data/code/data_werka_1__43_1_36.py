class Square:
    def __init__(self, side_length):
        if not isinstance(side_length, (int, float)) or side_length <= 0:
            raise ValueError("Side length must be a positive number")
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    try:
        sample_side_length = 7.5
        square = Square(sample_side_length)
        print(square.area())
    except ValueError as e:
        print(e)