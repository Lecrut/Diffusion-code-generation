class VolumeConverter:
    def __init__(self):
        self.base_unit = "L"
        self.factors = {
            "L": 1.0,
            "ml": 0.001,
            "m3": 1000.0,
            "gal": 3.785411784,
            "fl_oz": 0.0295735295625,
            "pt": 0.473176473,
            "qt": 0.946352946,
            "cup": 0.2365882365,
            "in3": 0.016387064,
            "ft3": 28.316846592,
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.factors:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_unit not in self.factors:
            raise ValueError(f"Unsupported target unit: {to_unit}")
        
        value_in_liters = value * self.factors[from_unit]
        result = value_in_liters / self.factors[to_unit]
        return result

if __name__ == "__main__":
    converter = VolumeConverter()
    sample_value = 5.0
    source = "m3"
    target = "gal"
    print(converter.convert(sample_value, source, target))
    print(converter.convert(1000, "ml", "L"))
    print(converter.convert(1, "L", "fl_oz"))