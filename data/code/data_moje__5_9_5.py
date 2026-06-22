class LengthComparator:
    def __init__(self, unit="meters"):
        self.unit = unit.lower()
        self.conversion_factors = {
            "meters": 1.0,
            "m": 1.0,
            "kilometers": 1000.0,
            "km": 1000.0,
            "centimeters": 0.01,
            "cm": 0.01,
            "millimeters": 0.001,
            "mm": 0.001,
            "miles": 1609.344,
            "mi": 1609.344,
            "yards": 0.9144,
            "yd": 0.9144,
            "feet": 0.3048,
            "ft": 0.3048,
            "inches": 0.0254,
            "in": 0.0254
        }

    def convert_to_meters(self, value, unit):
        unit_lower = unit.lower()
        if unit_lower not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * self.conversion_factors[unit_lower]

    def compare(self, value1, unit1, value2, unit2):
        meters1 = self.convert_to_meters(value1, unit1)
        meters2 = self.convert_to_meters(value2, unit2)
        
        if meters1 > meters2:
            return f"{value1} {unit1} is greater than {value2} {unit2}"
        elif meters1 < meters2:
            return f"{value1} {unit1} is less than {value2} {unit2}"
        else:
            return f"{value1} {unit1} is equal to {value2} {unit2}"

    def compare_detailed(self, value1, unit1, value2, unit2):
        meters1 = self.convert_to_meters(value1, unit1)
        meters2 = self.convert_to_meters(value2, unit2)
        difference = abs(meters1 - meters2)
        ratio = meters1 / meters2 if meters2 != 0 else float('inf')
        
        result = self.compare(value1, unit1, value2, unit2)
        return {
            "comparison": result,
            "value1_in_meters": meters1,
            "value2_in_meters": meters2,
            "difference_meters": difference,
            "ratio": ratio
        }

if __name__ == '__main__':
    comparator = LengthComparator()
    
    result1 = comparator.compare(5, "km", 3000, "m")
    print(result1)
    
    result2 = comparator.compare(100, "cm", 1, "m")
    print(result2)
    
    result3 = comparator.compare(1, "mile", 1, "km")
    print(result3)
    
    detailed_result = comparator.compare_detailed(10, "ft", 3, "m")
    print(detailed_result)