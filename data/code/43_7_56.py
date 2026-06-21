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
        sample_square1 = Square(5)
        print(f"Area of square with side 5: {sample_square1.compute_area()}")
        
        sample_square2 = Square(8.2)
        print(f"Area of square with side 8.2: {sample_square2.compute_area()}")
    except ValueError as e:
        print(e)