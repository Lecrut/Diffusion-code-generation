class LengthComparator:
    def __init__(self, unit):
        self.unit = unit
        self.meters_per_unit = {
            "mm": 0.001,
            "cm": 0.01,
            "m": 1.0,
            "km": 1000.0,
            "in": 0.0254,
            "ft": 0.3048,
            "yd": 0.9144,
            "mi": 1609.344,
        }

    def compare(self, value1, value2):
        if self.unit not in self.meters_per_unit:
            raise ValueError(f"Unsupported unit: {self.unit}")
        m1 = value1 * self.meters_per_unit[self.unit]
        m2 = value2 * self.meters_per_unit[self.unit]
        if m1 > m2:
            return f"{value1} {self.unit} is greater than {value2} {self.unit}"
        elif m1 < m2:
            return f"{value1} {self.unit} is less than {value2} {self.unit}"
        else:
            return f"{value1} {self.unit} is equal to {value2} {self.unit}"

if __name__ == '__main__':
    comparator = LengthComparator("m")
    result1 = comparator.compare(10.5, 12.0)
    print(result1)
    result2 = comparator.compare(5.0, 5.0)
    print(result2)
    result3 = comparator.compare(1.5, 1.0)
    print(result3)
    comparator_inch = LengthComparator("ft")
    result4 = comparator_inch.compare(10, 300)
    print(result4)