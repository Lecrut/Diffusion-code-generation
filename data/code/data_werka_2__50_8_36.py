class AreaDifference:
    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def validate_areas(self):
        if not (isinstance(self.area1, (int, float)) and isinstance(self.area2, (int, float))):
            raise ValueError("Both areas must be numbers.")

    def calculate_difference(self):
        self.validate_areas()
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    area_calculator = AreaDifference(90, 45)
    print(area_calculator.calculate_difference())