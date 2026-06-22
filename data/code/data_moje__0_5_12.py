class UnitConverter:
    def __init__(self, base_unit):
        self.base_unit = base_unit
        self.factors = {}

    def add_conversion(self, unit_name, factor_to_base):
        self.factors[unit_name] = factor_to_base

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.factors:
            raise ValueError(f"Unknown source unit: {from_unit}")
        if to_unit not in self.factors:
            raise ValueError(f"Unknown target unit: {to_unit}")
        
        base_value = value * self.factors[from_unit]
        result = base_value / self.factors[to_unit]
        return result

if __name__ == "__main__":
    converter = UnitConverter("meter")
    converter.add_conversion("meter", 1.0)
    converter.add_conversion("kilometer", 1000.0)
    converter.add_conversion("centimeter", 0.01)
    converter.add_conversion("inch", 0.0254)
    converter.add_conversion("foot", 0.3048)

    result_km_to_m = converter.convert(5.5, "kilometer", "meter")
    result_inch_to_cm = converter.convert(12.0, "inch", "centimeter")
    result_foot_to_kilometer = converter.convert(100.0, "foot", "kilometer")
    
    print(result_km_to_m)
    print(result_inch_to_cm)
    print(result_foot_to_kilometer)