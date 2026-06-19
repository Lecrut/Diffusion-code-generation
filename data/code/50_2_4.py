class AreaDifferenceCalculator:
    def __init__(self):
        self.units = {'sqm': 1, 'sqft': 0.092903}

    def convert_to_sqm(self, area, unit):
        return area * self.units.get(unit, 1)

    def calculate_difference(self, area1, area2, unit='sqm'):
        area1_sqm = self.convert_to_sqm(area1, unit)
        area2_sqm = self.convert_to_sqm(area2, unit)
        return abs(area1_sqm - area2_sqm)

if __name__ == '__main__':
    calculator = AreaDifferenceCalculator()
    area_a = 100
    area_b = 75
    difference = calculator.calculate_difference(area_a, area_b, 'sqm')
    print(difference)