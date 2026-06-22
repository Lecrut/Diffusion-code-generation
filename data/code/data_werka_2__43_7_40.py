class Square:
    def __init__(self, side_length):
        if not isinstance(side_length, (int, float)) or side_length < 0:
            raise ValueError("Side length must be a non-negative number")
        self.side_length = side_length

    def compute_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    try:
        sample_square = Square(3.5)
        print(f"The area of the square is: {sample_square.compute_area()}")
    except ValueError as e:
        print(e)