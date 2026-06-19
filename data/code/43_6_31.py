class Square:
    def __init__(self, side_length):
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    try:
        sample_square = Square(5)
        print(sample_square.area())
    except ValueError as e:
        print(e)