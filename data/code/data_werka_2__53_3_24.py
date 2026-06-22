import math

class SquareCalculator:
    MIN_AREA = 0.0

    @staticmethod
    def find_side_length(area):
        if area < SquareCalculator.MIN_AREA:
            raise ValueError("Area cannot be negative")
        return math.sqrt(area)

if __name__ == '__main__':
    sample_area = 64.0
    calculator = SquareCalculator()
    side_length = calculator.find_side_length(sample_area)
    print(side_length)