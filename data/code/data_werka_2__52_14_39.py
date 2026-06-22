class SquareCalculator:
    def __init__(self, side_length):
        self.side_length = side_length
        self.validate_side_length()

    def validate_side_length(self):
        if not isinstance(self.side_length, (int, float)):
            raise ValueError("Side length must be a number")
        if self.side_length < 0:
            raise ValueError("Side length cannot be negative")

    def calculate_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_side_length1 = 4
    calculator1 = SquareCalculator(sample_side_length1)
    area1 = calculator1.calculate_area()
    print(f"Area of square with side length {sample_side_length1}: {area1}")

    sample_side_length2 = 9
    calculator2 = SquareCalculator(sample_side_length2)
    area2 = calculator2.calculate_area()
    print(f"Area of square with side length {sample_side_length2}: {area2}")