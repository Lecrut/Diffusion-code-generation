class LengthComparator:
    def __init__(self):
        self.unit_multiplier = {
            'mm': 0.001,
            'cm': 0.01,
            'm': 1.0,
            'km': 1000.0,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.34
        }

    def compare(self, value1, unit1, value2, unit2):
        if unit1 not in self.unit_multiplier:
            raise ValueError(f"Unsupported unit: {unit1}")
        if unit2 not in self.unit_multiplier:
            raise ValueError(f"Unsupported unit: {unit2}")

        meters1 = value1 * self.unit_multiplier[unit1]
        meters2 = value2 * self.unit_multiplier[unit2]

        if meters1 > meters2:
            return 1
        elif meters1 < meters2:
            return -1
        else:
            return 0

    def describe_comparison(self, value1, unit1, value2, unit2):
        result_code = self.compare(value1, unit1, value2, unit2)
        if result_code == 1:
            return f"{value1} {unit1} is longer than {value2} {unit2}"
        elif result_code == -1:
            return f"{value1} {unit1} is shorter than {value2} {unit2}"
        else:
            return f"{value1} {unit1} is equal to {value2} {unit2}"

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.describe_comparison(100, 'cm', 1, 'm'))
    print(comparator.describe_comparison(5, 'ft', 2, 'm'))
    print(comparator.compare(10, 'm', 1000, 'cm'))