class Square:
    def __init__(self, side_length):
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_square_small = Square(3)
    print(f"The area of the small square is {sample_square_small.area()}")

    sample_square_medium = Square(7)
    print(f"The area of the medium square is {sample_square_medium.area()}")

    sample_square_large = Square(10)
    print(f"The area of the large square is {sample_square_large.area()}")