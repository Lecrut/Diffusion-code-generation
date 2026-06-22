class AreaCalculator:
    def __init__(self):
        self.default_area1 = 0.0
        self.default_area2 = 0.0

    def set_areas(self, area1, area2):
        self.default_area1 = area1
        self.default_area2 = area2

    def calculate_difference(self):
        return abs(self.default_area1 - self.default_area2)

if __name__ == '__main__':
    SAMPLE_AREA_1 = 300.75
    SAMPLE_AREA_2 = 240.25
    calculator = AreaCalculator()
    calculator.set_areas(SAMPLE_AREA_1, SAMPLE_AREA_2)
    difference = calculator.calculate_difference()
    print(difference)