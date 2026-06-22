class VolumeConverter:
    def __init__(self):
        self.units = {
            "liter": 1.0,
            "milliliter": 0.001,
            "cubic_meter": 1000.0,
            "gallon": 0.264172,
            "cubic_inch": 61.0237
        }

    def to_liters(self, value, unit):
        unit_lower = unit.lower()
        if unit_lower not in self.units:
            raise ValueError(f"Unknown unit: {unit}")
        return value / self.units[unit_lower]

    def from_liters(self, value, target_unit):
        target_lower = target_unit.lower()
        if target_lower not in self.units:
            raise ValueError(f"Unknown unit: {target_unit}")
        return value * self.units[target_lower]

    def convert(self, value, source_unit, target_unit):
        liters = self.to_liters(value, source_unit)
        return self.from_liters(liters, target_unit)

if __name__ == '__main__':
    converter = VolumeConverter()
    result1 = converter.convert(5, "gallon", "liter")
    result2 = converter.convert(1000, "milliliter", "liter")
    result3 = converter.convert(1, "cubic_meter", "gallon")
    result4 = converter.convert(10, "liter", "cubic_inch")
    result5 = converter.convert(50, "cubic_inch", "milliliter")
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)