class VolumeConverter:
    def __init__(self):
        self.base_unit = "ml"
        self.to_base_multiplier = {
            "ml": 1.0,
            "l": 1000.0,
            "gal": 3785.411784,
            "qt": 946.352946,
            "pt": 473.176473,
            "cup": 236.5882365,
            "fl_oz": 29.5735295625,
            "tbsp": 14.78676478125,
            "tsp": 4.92892159375,
            "m3": 1000000.0,
            "cm3": 1.0,
            "ft3": 28316.846592,
            "in3": 16.387064
        }

    def get_base_value(self, amount, unit):
        if unit not in self.to_base_multiplier:
            raise ValueError(f"Unsupported unit: {unit}")
        return amount * self.to_base_multiplier[unit]

    def convert(self, amount, source_unit, target_unit):
        if source_unit not in self.to_base_multiplier:
            raise ValueError(f"Unsupported source unit: {source_unit}")
        if target_unit not in self.to_base_multiplier:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        base_value = self.get_base_value(amount, source_unit)
        return base_value / self.to_base_multiplier[target_unit]

if __name__ == '__main__':
    converter = VolumeConverter()
    result1 = converter.convert(1.0, "l", "ml")
    result2 = converter.convert(5.0, "gal", "l")
    result3 = converter.convert(1.0, "m3", "ft3")
    print(result1)
    print(result2)
    print(result3)