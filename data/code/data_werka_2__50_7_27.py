class AreaCalculator:
    def __init__(self):
        self.units = {'square meters': 1, 'square feet': 0.092903}

    def get_difference(self, area_a, area_b, unit='square meters'):
        if not (isinstance(area_a, (int, float)) and isinstance(area_b, (int, float))):
            raise ValueError("Both areas must be numbers")
        if unit not in self.units:
            raise ValueError(f"Unsupported unit: {unit}")
        factor = self.units[unit]
        return abs((area_a * factor) - (area_b * factor))

if __name__ == '__main__':
    calculator = AreaCalculator()
    area1 = 25.0
    area2 = 30.0
    unit = 'square feet'
    difference = calculator.get_difference(area1, area2, unit)
    print(difference)