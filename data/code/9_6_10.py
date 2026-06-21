class VolumeConverter:
    def __init__(self):
        self.base_unit = "L"
        self.to_base_factors = {
            "L": 1.0,
            "ml": 0.001,
            "m3": 1000.0,
            "gal_us": 3.785411784,
            "gal_uk": 4.54609,
            "qt_us": 0.946352946,
            "pt_us": 0.473176473,
            "cup_us": 0.2365882365,
            "fl_oz_us": 0.0295735295625,
            "tbsp_us": 0.01478676478125,
            "tsp_us": 0.00492892159375,
            "in3": 0.016387064,
            "ft3": 28.316846592,
            "cm3": 0.001,
            "cc": 0.001
        }

    def _validate_unit(self, unit):
        if unit not in self.to_base_factors:
            raise ValueError(f"Unit '{unit}' is not supported.")

    def convert(self, value, from_unit, to_unit):
        self._validate_unit(from_unit)
        self._validate_unit(to_unit)
        
        if from_unit == to_unit:
            return value
            
        liters = value * self.to_base_factors[from_unit]
        result = liters / self.to_base_factors[to_unit]
        return result

    def get_available_units(self):
        return list(self.to_base_factors.keys())

if __name__ == '__main__':
    converter = VolumeConverter()
    result1 = converter.convert(1.0, "L", "ml")
    result2 = converter.convert(1.0, "m3", "gal_us")
    result3 = converter.convert(1.0, "gal_uk", "L")
    result4 = converter.convert(500.0, "ml", "cup_us")
    print(result1)
    print(result2)
    print(result3)
    print(result4)