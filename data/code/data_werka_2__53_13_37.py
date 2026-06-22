import math

class SquareCalculator:
    def __init__(self):
        self.area = 0

    def set_area(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.area = area

    def calculate_side_length(self):
        return math.sqrt(self.area)

if __name__ == '__main__':
    calculator = SquareCalculator()
    sample_areas = [16, 25, 81]
    for area in sample_areas:
        calculator.set_area(area)
        side_length = calculator.calculate_side_length()
        print(side_length)