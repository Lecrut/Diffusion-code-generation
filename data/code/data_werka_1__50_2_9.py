class AreaDifferenceCalculator:
    def __init__(self):
        self.area1 = 0
        self.area2 = 0

    def validate_areas(self, area1, area2):
        if not isinstance(area1, (int, float)) or not isinstance(area2, (int, float)):
            raise ValueError("Both areas must be either integers or floats.")
        return True

    def calculate_difference(self, area1, area2):
        self.validate_areas(area1, area2)
        self.area1 = area1
        self.area2 = area2
        return abs(area1 - area2)

if __name__ == '__main__':
    calculator = AreaDifferenceCalculator()
    area_a = 120
    area_b = 45.3
    try:
        difference = calculator.calculate_difference(area_a, area_b)
        print(difference)
    except ValueError as e:
        print(e)