class LengthComparator:
    def __init__(self, unit1, unit2):
        self.unit1 = unit1
        self.unit2 = unit2

    def convert_to_meters(self, value, unit):
        conversions = {
            "m": 1.0,
            "cm": 0.01,
            "mm": 0.001,
            "km": 1000.0,
            "in": 0.0254,
            "ft": 0.3048,
            "yd": 0.9144,
            "mi": 1609.34
        }
        if unit not in conversions:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * conversions[unit]

    def compare(self, value1, value2):
        meters1 = self.convert_to_meters(value1, self.unit1)
        meters2 = self.convert_to_meters(value2, self.unit2)
        
        if meters1 > meters2:
            result = "greater than"
        elif meters1 < meters2:
            result = "less than"
        else:
            result = "equal to"
        
        return f"{value1} {self.unit1} is {result} {value2} {self.unit2}"

if __name__ == '__main__':
    comparator = LengthComparator("m", "cm")
    result = comparator.compare(1, 100)
    print(result)