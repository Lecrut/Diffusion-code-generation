class Square:
    def __init__(self, side_length: float):
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        self.side_length = side_length

    def area(self) -> float:
        return self.side_length ** 2

if __name__ == '__main__':
    sample_side_length1 = 4.0
    square1 = Square(sample_side_length1)
    print(square1.area())

    sample_side_length2 = 6.5
    square2 = Square(sample_side_length2)
    print(square2.area())