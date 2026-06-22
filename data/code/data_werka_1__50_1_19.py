class AreaCalculator:
    def __init__(self):
        self.units = {
            'square_meters': 1,
            'square_feet': 0.092903,
            'hectares': 10000
        }

    def convert_to_square_meters(self, area, unit):
        return area * self.units.get(unit, 1)

    def calculate_difference(self, area1, area2, unit1='square_meters', unit2='square_meters'):
        area1_meters = self.convert_to_square_meters(area1, unit1)
        area2_meters = self.convert_to_square_meters(area2, unit2)
        return abs(area1_meters - area2_meters)

if __name__ == '__main__':
    calculator = AreaCalculator()
    a = 50
    b = 100
    result = calculator.calculate_difference(a, b, 'hectares', 'square_feet')
    print(result)