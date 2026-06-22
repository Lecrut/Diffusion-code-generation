class Square:
    MIN_SIDE_LENGTH = 0

    def __init__(self, side_length):
        if side_length < self.MIN_SIDE_LENGTH:
            raise ValueError("Side length cannot be negative")
        self.side_length = side_length

    def compute_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    try:
        sample_square1 = Square(8)
        print(f"The area of the square with side length {sample_square1.side_length} is: {sample_square1.compute_area()}")

        sample_square2 = Square(10.5)
        print(f"The area of the square with side length {sample_square2.side_length} is: {sample_square2.compute_area()}")
    except ValueError as e:
        print(e)