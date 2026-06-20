class UnitConverter:
    def __init__(self):
        self.base_unit = "meter"
        self.factors = {
            "meter": 1.0,
            "kilometer": 1000.0,
            "centimeter": 0.01,
            "millimeter": 0.001,
            "mile": 1609.344,
            "yard": 0.9144,
            "foot": 0.3048,
            "inch": 0.0254
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.factors:
            raise ValueError(f"Unknown source unit: {from_unit}")
        if to_unit not in self.factors:
            raise ValueError(f"Unknown target unit: {to_unit}")
        
        base_value = value * self.factors[from_unit]
        result = base_value / self.factors[to_unit]
        return result

if __name__ == '__main__':
    converter = UnitConverter()
    result_m_to_km = converter.convert(1500, "meter", "kilometer")
    print(result_m_to_km)
    result_mi_to_m = converter.convert(1, "mile", "meter")
    print(result_mi_to_m)
    result_ft_to_cm = converter.convert(6, "foot", "centimeter")
    print(result_ft_to_cm)
    result_yd_to_mm = converter.convert(2.5, "yard", "millimeter")
    print(result_yd_to_mm)