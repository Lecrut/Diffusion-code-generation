class VolumeConverter:
    BASE_UNIT = "liter"
    
    def __init__(self):
        self._factors_to_base = {
            "ml": 0.001,
            "liter": 1.0,
            "m3": 1000.0,
            "gal": 3.785411784,
            "qt": 0.946352946,
            "pt": 0.473176473,
            "cup": 0.2365882365,
            "fl_oz": 0.0295735295625,
            "tbsp": 0.01478676478125,
            "tsp": 0.00492892159375,
            "cm3": 0.001,
            "in3": 0.016387064,
            "ft3": 28.316846592
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self._factors_to_base:
            raise ValueError(f"Unknown source unit: {from_unit}")
        if to_unit not in self._factors_to_base:
            raise ValueError(f"Unknown target unit: {to_unit}")
        
        value_in_base = value * self._factors_to_base[from_unit]
        result = value_in_base / self._factors_to_base[to_unit]
        return result

    def get_conversion_factor(self, from_unit, to_unit):
        if from_unit not in self._factors_to_base:
            raise ValueError(f"Unknown source unit: {from_unit}")
        if to_unit not in self._factors_to_base:
            raise ValueError(f"Unknown target unit: {to_unit}")
        
        from_factor = self._factors_to_base[from_unit]
        to_factor = self._factors_to_base[to_unit]
        return from_factor / to_factor

if __name__ == "__main__":
    converter = VolumeConverter()
    result1 = converter.convert(1.0, "liter", "ml")
    result2 = converter.convert(1.0, "m3", "gal")
    result3 = converter.convert(5.0, "qt", "liter")
    print(result1)
    print(result2)
    print(result3)