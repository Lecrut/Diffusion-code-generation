class AreaCalculator:
    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def validate_areas(self):
        if not (isinstance(self.area1, (int, float)) and isinstance(self.area2, (int, float))):
            raise ValueError("Both areas must be numbers.")
        if self.area1 < 0 or self.area2 < 0:
            raise ValueError("Areas cannot be negative.")

    def calculate_difference(self):
        self.validate_areas()
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    area1 = 75.3
    area2 = 24.8
    calculator = AreaCalculator(area1, area2)
    difference = calculator.calculate_difference()
    print(difference)