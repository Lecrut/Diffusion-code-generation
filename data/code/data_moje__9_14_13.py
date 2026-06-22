class VolumeConverter:
    CONVERSIONS = {
        'liters': 1.0,
        'milliliters': 1000.0,
        'gallons': 0.264172,
        'quarts': 1.05669,
        'pints': 2.11338,
        'cups': 4.22675,
        'fluid_ounces': 33.814
    }

    def __init__(self):
        self.supported_units = list(self.CONVERSIONS.keys())

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.CONVERSIONS:
            raise ValueError(f"Unsupported unit: {from_unit}")
        if to_unit not in self.CONVERSIONS:
            raise ValueError(f"Unsupported unit: {to_unit}")

        liters = value / self.CONVERSIONS[from_unit]
        result = liters * self.CONVERSIONS[to_unit]
        return result

if __name__ == '__main__':
    converter = VolumeConverter()
    result1 = converter.convert(1, 'liters', 'gallons')
    print(result1)
    result2 = converter.convert(500, 'milliliters', 'cups')
    print(result2)
    result3 = converter.convert(1, 'gallons', 'liters')
    print(result3)
    result4 = converter.convert(8, 'fluid_ounces', 'milliliters')
    print(result4)
    result5 = converter.convert(2, 'quarts', 'pints')
    print(result5)