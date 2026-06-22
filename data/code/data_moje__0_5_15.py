class UnitConverter:
    def __init__(self):
        self.base_unit = "meters"
        self.factors = {
            "meters": 1.0,
            "kilometers": 1000.0,
            "centimeters": 0.01,
            "millimeters": 0.001,
            "feet": 0.3048,
            "inches": 0.0254,
            "yards": 0.9144,
            "miles": 1609.344
        }

    def convert(self, value, from_unit, to_unit):
        from_unit_lower = from_unit.lower()
        to_unit_lower = to_unit.lower()
        
        if from_unit_lower not in self.factors:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit_lower not in self.factors:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        base_value = value * self.factors[from_unit_lower]
        result_value = base_value / self.factors[to_unit_lower]
        
        return result_value

if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.convert(5, "miles", "kilometers")
    print(f"5 miles equals {result} kilometers")
    
    result2 = converter.convert(100, "centimeters", "feet")
    print(f"100 centimeters equals {result2} feet")
    
    result3 = converter.convert(12, "inches", "meters")
    print(f"12 inches equals {result3} meters")