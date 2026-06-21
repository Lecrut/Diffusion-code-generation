class Square:
    def __init__(self, side_length):
        self.side_length = side_length
        self.validate_side_length()

    def validate_side_length(self):
        if not isinstance(self.side_length, (int, float)):
            raise ValueError("Side length must be a number")
        if self.side_length < 0:
            raise ValueError("Side length cannot be negative")

    def get_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_side_length_1 = 4
    square_1 = Square(sample_side_length_1)
    area_1 = square_1.get_area()
    print(area_1)

    sample_side_length_2 = 9
    square_2 = Square(sample_side_length_2)
    area_2 = square_2.get_area()
    print(area_2)