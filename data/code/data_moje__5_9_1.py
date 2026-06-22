class LengthComparator:
    def __init__(self, value1, unit1, value2, unit2):
        self.value1 = value1
        self.unit1 = unit1
        self.value2 = value2
        self.unit2 = unit2

    def convert_to_meters(self, value, unit):
        conversions = {
            'mm': 0.001,
            'cm': 0.01,
            'm': 1.0,
            'km': 1000.0,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.34
        }
        return value * conversions[unit.lower()]

    def compare(self):
        length1_meters = self.convert_to_meters(self.value1, self.unit1)
        length2_meters = self.convert_to_meters(self.value2, self.unit2)

        if length1_meters > length2_meters:
            return f"{self.value1} {self.unit1} is longer than {self.value2} {self.unit2}"
        elif length1_meters < length2_meters:
            return f"{self.value1} {self.unit1} is shorter than {self.value2} {self.unit2}"
        else:
            return f"{self.value1} {self.unit1} is equal to {self.value2} {self.unit2}"

if __name__ == '__main__':
    comparator = LengthComparator(1, 'km', 1000, 'm')
    result = comparator.compare()
    print(result)

    comparator2 = LengthComparator(5, 'ft', 1.5, 'm')
    result2 = comparator2.compare()
    print(result2)

    comparator3 = LengthComparator(100, 'cm', 1, 'm')
    result3 = comparator3.compare()
    print(result3)