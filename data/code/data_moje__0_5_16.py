class UnitConverter:
    def __init__(self):
        self.base_unit = "meter"
        self.factors = {
            "meter": 1.0,
            "kilometer": 1000.0,
            "centimeter": 0.01,
            "millimeter": 0.001,
            "inch": 0.0254,
            "foot": 0.3048,
            "yard": 0.9144,
            "mile": 1609.344,
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.factors:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self.factors:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        base_value = value * self.factors[from_unit]
        result = base_value / self.factors[to_unit]
        return result

if __name__ == '__main__':
    converter = UnitConverter()
    meters_to_kilometers = converter.convert(5000, "meter", "kilometer")
    feet_to_meters = converter.convert(100, "foot", "meter")
    miles_to_meters = converter.convert(2, "mile", "meter")
    kilometers_to_inches = converter.convert(1, "kilometer", "inch")
    
    print(meters_to_kilometers)
    print(feet_to_meters)
    print(miles_to_meters)
    print(kilometers_to_inches)