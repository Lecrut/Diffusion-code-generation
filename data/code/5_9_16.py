class LengthComparator:
    def __init__(self, value1, unit1, value2, unit2):
        self.value1 = value1
        self.unit1 = unit1.lower()
        self.value2 = value2
        self.unit2 = unit2.lower()

    def _convert_to_meters(self, value, unit):
        conversion_factors = {
            'meter': 1.0,
            'meters': 1.0,
            'm': 1.0,
            'kilometer': 1000.0,
            'kilometers': 1000.0,
            'km': 1000.0,
            'centimeter': 0.01,
            'centimeters': 0.01,
            'cm': 0.01,
            'millimeter': 0.001,
            'millimeters': 0.001,
            'mm': 0.001,
            'mile': 1609.34,
            'miles': 1609.34,
            'foot': 0.3048,
            'feet': 0.3048,
            'ft': 0.3048,
            'inch': 0.0254,
            'inches': 0.0254,
            'in': 0.0254,
            'yard': 0.9144,
            'yards': 0.9144,
            'yd': 0.9144
        }
        return value * conversion_factors[unit]

    def compare(self):
        meters1 = self._convert_to_meters(self.value1, self.unit1)
        meters2 = self._convert_to_meters(self.value2, self.unit2)

        if meters1 > meters2:
            return f"{self.value1} {self.unit1} is greater than {self.value2} {self.unit2}"
        elif meters1 < meters2:
            return f"{self.value1} {self.unit1} is less than {self.value2} {self.unit2}"
        else:
            return f"{self.value1} {self.unit1} is equal to {self.value2} {self.unit2}"

if __name__ == '__main__':
    comparator = LengthComparator(1, 'meter', 100, 'centimeter')
    print(comparator.compare())

    comparator2 = LengthComparator(1, 'mile', 1609, 'meter')
    print(comparator2.compare())

    comparator3 = LengthComparator(10, 'feet', 3, 'meters')
    print(comparator3.compare())