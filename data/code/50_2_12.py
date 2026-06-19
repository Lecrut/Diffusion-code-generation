class AreaDifferenceCalculator:
    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def calculate_difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    sample_areas = {
        'area_a': 100,
        'area_b': 45
    }
    calculator = AreaDifferenceCalculator(sample_areas['area_a'], sample_areas['area_b'])
    difference = calculator.calculate_difference()
    print(difference)