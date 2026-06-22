class LengthComparator:
    def __init__(self):
        self.supported_units = ['mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mi']
        self.to_meters = {
            'mm': 0.001,
            'cm': 0.01,
            'm': 1.0,
            'km': 1000.0,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.344
        }

    def convert_to_meters(self, value, unit):
        if unit not in self.supported_units:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * self.to_meters[unit]

    def compare(self, value1, unit1, value2, unit2):
        m1 = self.convert_to_meters(value1, unit1)
        m2 = self.convert_to_meters(value2, unit2)
        if m1 > m2:
            return f"{value1} {unit1} is greater than {value2} {unit2}"
        elif m1 < m2:
            return f"{value1} {unit1} is less than {value2} {unit2}"
        else:
            return f"{value1} {unit1} is equal to {value2} {unit2}"

if __name__ == '__main__':
    comparator = LengthComparator()
    result1 = comparator.compare(100, 'cm', 1, 'm')
    print(result1)
    result2 = comparator.compare(1, 'km', 500, 'm')
    print(result2)
    result3 = comparator.compare(10, 'in', 2, 'ft')
    print(result3)