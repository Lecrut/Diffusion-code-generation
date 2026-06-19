class SquareCalculator:
    def __init__(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.area = area

    @staticmethod
    def find_side_length(area):
        return area ** 0.5

if __name__ == '__main__':
    sample_area = 16
    calculator = SquareCalculator(sample_area)
    side_length = calculator.find_side_length(calculator.area)
    print(f"The side length of the square with area {sample_area} is: {side_length}")