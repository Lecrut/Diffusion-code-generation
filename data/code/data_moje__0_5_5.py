class UnitConverter:
    def __init__(self, base_unit, factors):
        self.base_unit = base_unit
        self.factors = factors
        if base_unit not in factors:
            raise ValueError("Base unit must be in the factors dictionary")
        if factors[base_unit] != 1.0:
            raise ValueError("Base unit conversion factor must be 1.0")

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.factors:
            raise ValueError(f"Unknown source unit: {from_unit}")
        if to_unit not in self.factors:
            raise ValueError(f"Unknown target unit: {to_unit}")
        
        base_value = value * self.factors[from_unit]
        converted_value = base_value / self.factors[to_unit]
        return converted_value

def run_samples():
    factors = {
        "m": 1.0,
        "km": 1000.0,
        "cm": 0.01,
        "mm": 0.001,
        "inch": 0.0254,
        "ft": 0.3048,
        "mi": 1609.344
    }
    
    converter = UnitConverter("m", factors)
    
    result1 = converter.convert(1, "km", "m")
    print(f"1 km in m: {result1}")
    
    result2 = converter.convert(1, "m", "inch")
    print(f"1 m in inch: {result2}")
    
    result3 = converter.convert(5280, "ft", "mi")
    print(f"5280 ft in mi: {result3}")
    
    result4 = converter.convert(100, "cm", "mm")
    print(f"100 cm in mm: {result4}")

if __name__ == '__main__':
    run_samples()