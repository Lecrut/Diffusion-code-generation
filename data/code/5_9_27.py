class LengthComparator:
    def __init__(self, length1, unit1, length2, unit2):
        self.length1 = length1
        self.unit1 = unit1.lower()
        self.length2 = length2
        self.unit2 = unit2.lower()

    def convert_to_meters(self, length, unit):
        conversion_factors = {
            'm': 1,
            'cm': 0.01,
            'mm': 0.001,
            'km': 1000,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144
        }
        return length * conversion_factors.get(unit, 0)

    def compare(self):
        length1_meters = self.convert_to_meters(self.length1, self.unit1)
        length2_meters = self.convert_to_meters(self.length2, self.unit2)

        if length1_meters > length2_meters:
            return f"{self.length1} {self.unit1} is greater than {self.length2} {self.unit2}"
        elif length1_meters < length2_meters:
            return f"{self.length1} {self.unit1} is less than {self.length2} {self.unit2}"
        else:
            return f"{self.length1} {self.unit1} is equal to {self.length2} {self.unit2}"

if __name__ == '__main__':
    comparator = LengthComparator(5, 'm', 100, 'cm')
    print(comparator.compare())