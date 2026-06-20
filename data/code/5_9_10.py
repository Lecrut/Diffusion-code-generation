class LengthComparator:
    def compare(self, length1, unit1, length2, unit2):
        conversions = {
            'mm': 0.001,
            'cm': 0.01,
            'm': 1,
            'km': 1000,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.344
        }

        if unit1 not in conversions or unit2 not in conversions:
            raise ValueError("Unsupported unit")

        meters1 = length1 * conversions[unit1]
        meters2 = length2 * conversions[unit2]

        if meters1 > meters2:
            return f"{length1} {unit1} is longer than {length2} {unit2}"
        elif meters1 < meters2:
            return f"{length1} {unit1} is shorter than {length2} {unit2}"
        else:
            return f"{length1} {unit1} is equal to {length2} {unit2}"

if __name__ == '__main__':
    comparator = LengthComparator()
    result1 = comparator.compare(100, 'cm', 1, 'm')
    print(result1)
    result2 = comparator.compare(5, 'ft', 1, 'm')
    print(result2)
    result3 = comparator.compare(10, 'km', 6, 'mi')
    print(result3)