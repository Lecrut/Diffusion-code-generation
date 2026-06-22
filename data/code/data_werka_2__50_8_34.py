class AreaDifferenceCalculator:
    def __init__(self, area1, area2):
        self.validate_area(area1)
        self.validate_area(area2)
        self.area1 = area1
        self.area2 = area2

    def validate_area(self, area):
        if not isinstance(area, (int, float)):
            raise ValueError("Area must be a number.")

    def calculate_difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    calculator = AreaDifferenceCalculator(90, 55)
    print(calculator.calculate_difference())