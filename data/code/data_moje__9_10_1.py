class VolumeConverter:
    LITERS_PER_UNIT = {
        'liter': 1.0,
        'milliliter': 0.001,
        'cubic_meter': 1000.0,
        'gallon_us': 3.785411784,
        'quart_us': 0.946352946,
        'pint_us': 0.473176473,
        'cup_us': 0.2365882365,
        'fluid_ounce_us': 0.0295735295625,
        'tablespoon_us': 0.01478676478125,
        'teaspoon_us': 0.00492892159375,
        'cubic_foot': 28.316846592,
        'cubic_inch': 0.016387064,
        'liter_uk': 1.0,
        'gallon_uk': 4.54609,
        'quart_uk': 1.1365225,
        'pint_uk': 0.56826125,
        'fluid_ounce_uk': 0.0284130625,
        'tablespoon_uk': 0.0177581715625,
        'teaspoon_uk': 0.005919390520833333,
    }

    VALID_UNITS = set(LITERS_PER_UNIT.keys())

    def to_base(self, value, unit):
        if unit not in self.VALID_UNITS:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * self.LITERS_PER_UNIT[unit]

    def from_base(self, value, unit):
        if unit not in self.VALID_UNITS:
            raise ValueError(f"Unsupported unit: {unit}")
        return value / self.LITERS_PER_UNIT[unit]

    def convert(self, value, source_unit, target_unit):
        liters = self.to_base(value, source_unit)
        return self.from_base(liters, target_unit)

if __name__ == '__main__':
    converter = VolumeConverter()
    gallons_to_liters = converter.to_base(5, 'gallon_us')
    liters_to_pints = converter.from_base(10, 'pint_us')
    gallons_to_pints = converter.convert(1, 'gallon_us', 'pint_us')
    cubic_meters_to_gallons_uk = converter.convert(2, 'cubic_meter', 'gallon_uk')
    print(gallons_to_liters)
    print(liters_to_pints)
    print(gallons_to_pints)
    print(cubic_meters_to_gallons_uk)