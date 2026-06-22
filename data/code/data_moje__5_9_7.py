class LengthComparator:
    def __init__(self, unit_conversion_rates=None):
        self.unit_conversion_rates = unit_conversion_rates or {
            'm': 1.0,
            'cm': 0.01,
            'mm': 0.001,
            'km': 1000.0,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.344
        }

    def compare(self, value1, unit1, value2, unit2):
        if unit1 not in self.unit_conversion_rates:
            raise ValueError(f"Unsupported unit: {unit1}")
        if unit2 not in self.unit_conversion_rates:
            raise ValueError(f"Unsupported unit: {unit2}")

        meters1 = value1 * self.unit_conversion_rates[unit1]
        meters2 = value2 * self.unit_conversion_rates[unit2]

        difference = meters1 - meters2

        if difference > 0:
            return f"{value1} {unit1} is greater than {value2} {unit2}"
        elif difference < 0:
            return f"{value1} {unit1} is less than {value2} {unit2}"
        else:
            return f"{value1} {unit1} is equal to {value2} {unit2}"

    def get_meters(self, value, unit):
        if unit not in self.unit_conversion_rates:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * self.unit_conversion_rates[unit]

if __name__ == '__main__':
    comparator = LengthComparator()
    result1 = comparator.compare(1, 'm', 100, 'cm')
    print(result1)
    result2 = comparator.compare(1, 'ft', 1, 'm')
    print(result2)
    result3 = comparator.compare(2.5, 'km', 2500, 'm')
    print(result3)
    meters_from_miles = comparator.get_meters(1, 'mi')
    print(meters_from_miles)