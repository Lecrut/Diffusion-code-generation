class VolumeConverter:
    def __init__(self):
        self.conversion_to_base = {
            'liters': 1.0,
            'milliliters': 0.001,
            'cubic_meters': 1000.0,
            'cubic_centimeters': 0.001,
            'gallons': 3.78541,
            'quarts': 0.946353,
            'pints': 0.473176,
            'cups': 0.236588,
            'fluid_ounces': 0.0295735,
            'tablespoons': 0.0147868,
            'teaspoons': 0.00492892
        }
        self.conversion_from_base = {
            k: 1.0 / v for k, v in self.conversion_to_base.items()
        }

    def convert_to_base(self, value, from_unit):
        from_unit = from_unit.lower().replace(' ', '_')
        if from_unit not in self.conversion_to_base:
            raise ValueError(f"Unsupported unit: {from_unit}")
        return value * self.conversion_to_base[from_unit]

    def convert_from_base(self, value, to_unit):
        to_unit = to_unit.lower().replace(' ', '_')
        if to_unit not in self.conversion_from_base:
            raise ValueError(f"Unsupported unit: {to_unit}")
        return value * self.conversion_from_base[to_unit]

    def convert(self, value, from_unit, to_unit):
        base_value = self.convert_to_base(value, from_unit)
        return self.convert_from_base(base_value, to_unit)

if __name__ == '__main__':
    converter = VolumeConverter()
    result = converter.convert(100, 'milliliters', 'liters')
    print(result)
    result2 = converter.convert(1, 'gallons', 'liters')
    print(result2)
    result3 = converter.convert(1000, 'liters', 'cubic_meters')
    print(result3)