class VolumeConverter:
    LITER_PER_MILLILITER = 0.001
    LITER_PER_CUBIC_METER = 1000.0
    LITER_PER_CUBIC_INCH = 0.016387064
    LITER_PER_CUBIC_FOOT = 28.316846592
    LITER_PER_GALLON_US = 3.785411784
    LITER_PER_QUART_US = 0.946352946
    LITER_PER_PINT_US = 0.473176473
    LITER_PER_CUP_US = 0.2365882365
    LITER_PER_TABLESPOON_US = 0.0147867648
    LITER_PER_TEASPOON_US = 0.0049289216
    SUPPORTED_UNITS = {
        'ml': LITER_PER_MILLILITER,
        'l': 1.0,
        'm3': LITER_PER_CUBIC_METER,
        'in3': LITER_PER_CUBIC_INCH,
        'ft3': LITER_PER_CUBIC_FOOT,
        'gal': LITER_PER_GALLON_US,
        'qt': LITER_PER_QUART_US,
        'pt': LITER_PER_PINT_US,
        'cup': LITER_PER_CUP_US,
        'tbsp': LITER_PER_TABLESPOON_US,
        'tsp': LITER_PER_TEASPOON_US,
    }

    def to_base_unit(self, value, unit):
        unit_lower = unit.lower()
        if unit_lower not in self.SUPPORTED_UNITS:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * self.SUPPORTED_UNITS[unit_lower]

    def from_base_unit(self, value, target_unit):
        target_lower = target_unit.lower()
        if target_lower not in self.SUPPORTED_UNITS:
            raise ValueError(f"Unsupported unit: {target_unit}")
        return value / self.SUPPORTED_UNITS[target_lower]

    def convert(self, value, source_unit, target_unit):
        if source_unit.lower() == target_unit.lower():
            return value
        liters = self.to_base_unit(value, source_unit)
        return self.from_base_unit(liters, target_unit)

if __name__ == '__main__':
    converter = VolumeConverter()
    gallons_to_liters = converter.convert(5.0, 'gal', 'l')
    liters_to_milliliters = converter.convert(2.5, 'l', 'ml')
    cubic_feet_to_gallons = converter.convert(1.0, 'ft3', 'gal')
    print(gallons_to_liters)
    print(liters_to_milliliters)
    print(cubic_feet_to_gallons)