class LengthComparator:
    def __init__(self, value1, unit1, value2, unit2):
        self.value1 = value1
        self.unit1 = unit1.lower()
        self.value2 = value2
        self.unit2 = unit2.lower()
        self.conversion_factors = {
            'cm': 0.01,
            'm': 1.0,
            'km': 1000.0,
            'in': 0.0254,
            'ft': 0.3048,
            'mi': 1609.344
        }

    def _to_meters(self, value, unit):
        if unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * self.conversion_factors[unit]

    def compare(self):
        meters1 = self._to_meters(self.value1, self.unit1)
        meters2 = self._to_meters(self.value2, self.unit2)
        
        if meters1 > meters2:
            return f"{self.value1} {self.unit1} is greater than {self.value2} {self.unit2}"
        elif meters1 < meters2:
            return f"{self.value1} {self.unit1} is less than {self.value2} {self.unit2}"
        else:
            return f"{self.value1} {self.unit1} is equal to {self.value2} {self.unit2}"

if __name__ == '__main__':
    comparator = LengthComparator(100, 'cm', 1, 'm')
    result = comparator.compare()
    print(result)