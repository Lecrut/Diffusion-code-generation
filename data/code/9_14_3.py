class VolumeConverter:
    def __init__(self):
        self.base = 'milliliters'
        self.conversion_to_ml = {
            'liters': 1000.0,
            'milliliters': 1.0,
            'gallons': 3785.411784,
            'quarts': 946.352946,
            'pints': 473.176473,
            'cups': 236.5882365,
            'fluid_ounces': 29.5735295625
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_to_ml:
            raise ValueError(f"Unsupported from_unit: {from_unit}")
        if to_unit not in self.conversion_to_ml:
            raise ValueError(f"Unsupported to_unit: {to_unit}")

        value_in_ml = value * self.conversion_to_ml[from_unit]
        result = value_in_ml / self.conversion_to_ml[to_unit]
        return result

if __name__ == '__main__':
    converter = VolumeConverter()
    result1 = converter.convert(1, 'liters', 'gallons')
    print(result1)
    result2 = converter.convert(500, 'milliliters', 'cups')
    print(result2)
    result3 = converter.convert(2, 'gallons', 'liters')
    print(result3)