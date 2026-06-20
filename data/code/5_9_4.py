class LengthComparator:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def to_meters(self):
        conversions = {
            'm': 1,
            'cm': 0.01,
            'mm': 0.001,
            'km': 1000,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.344
        }
        unit_lower = self.unit.lower()
        if unit_lower in conversions:
            return self.value * conversions[unit_lower]
        raise ValueError(f"Unknown unit: {self.unit}")

    def compare(self, other):
        self_meters = self.to_meters()
        other_meters = other.to_meters()
        if self_meters < other_meters:
            return "Less than"
        elif self_meters > other_meters:
            return "Greater than"
        else:
            return "Equal to"

if __name__ == '__main__':
    l1 = LengthComparator(100, 'cm')
    l2 = LengthComparator(1, 'm')
    comparator = LengthComparator(1, 'm')
    other = LengthComparator(100, 'cm')
    result = comparator.compare(other)
    print(result)