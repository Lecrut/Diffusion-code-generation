class AreaDifferenceCalculator:
    def __init__(self):
        self.areas_validated = False

    def validate_areas(self, area1, area2):
        if not isinstance(area1, (int, float)) or not isinstance(area2, (int, float)):
            raise ValueError("Both areas must be numbers.")
        self.areas_validated = True
        return True

    def calculate_difference(self, area1, area2):
        if not self.areas_validated:
            self.validate_areas(area1, area2)
        return abs(area1 - area2)

if __name__ == '__main__':
    calculator = AreaDifferenceCalculator()
    area_a = 120
    area_b = 78
    difference = calculator.calculate_difference(area_a, area_b)
    print(difference)