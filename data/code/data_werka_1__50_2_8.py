class AreaDifference:
    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def calculate(self):
        return self.area1 - self.area2

if __name__ == '__main__':
    sample_areas = {'area_a': 200, 'area_b': 100}
    diff_calculator = AreaDifference(sample_areas['area_a'], sample_areas['area_b'])
    difference = diff_calculator.calculate()
    print(difference)