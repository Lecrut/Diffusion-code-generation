class Square:
    def __init__(self, side_length: float):
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        self.side_length = side_length

    def calculate_area(self) -> float:
        return self.side_length ** 2

if __name__ == '__main__':
    sample_side_length = 4.5
    square = Square(sample_side_length)
    area = square.calculate_area()
    print(area)

    another_sample_side_length = 6.0
    another_square = Square(another_sample_side_length)
    another_area = another_square.calculate_area()
    print(another_area)