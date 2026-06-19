class LengthComparator:

    def __init__(self, value1, unit1, value2, unit2):
        self.value1 = value1
        self.unit1 = unit1
        self.value2 = value2
        self.unit2 = unit2

    def compare(self):
        value1_in_meters = self._convert_to_meters(self.value1, self.unit1)
        value2_in_meters = self._convert_to_meters(self.value2, self.unit2)
        if value1_in_meters > value2_in_meters:
            return f'{self.value1} {self.unit1} is greater than {self.value2} {self.unit2}'
        elif value1_in_meters < value2_in_meters:
            return f'{self.value1} {self.unit1} is less than {self.value2} {self.unit2}'
        else:
            return f'{self.value1} {self.unit1} is equal to {self.value2} {self.unit2}'

    def _convert_to_meters(self, value, unit):
        conversion_factors = {'m': 1, 'cm': 0.01, 'mm': 0.001, 'km': 1000, 'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144}
        return value * conversion_factors[unit]
if __name__ == '__main__':
    comparator = LengthComparator(10, 'cm', 1, 'm')
    print(comparator.compare())