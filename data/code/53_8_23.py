class SquareCalculator:
    def __init__(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.area = area

    def calculate_side_length(self):
        return self.area ** 0.5

if __name__ == '__main__':
    sample_area = 25.0
    calculator = SquareCalculator(sample_area)
    side_length = calculator.calculate_side_length()
    print(side_length)