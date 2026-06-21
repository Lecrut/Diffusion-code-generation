class VolumeConverter:
    BASE_UNIT = 'liter'
    CONVERSION_FACTORS = {
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
        'cubic_inch': 0.016387064,
        'cubic_foot': 28.316846592,
        'cubic_yard': 764.554857984,
        'imperial_gallon': 4.54609,
        'imperial_quart': 1.1365225,
        'imperial_pint': 0.56826125,
        'imperial_fluid_ounce': 0.0284130625,
        'imperial_tablespoon': 0.0177581640625,
        'imperial_teaspoon': 0.0059193880208333,
    }

    def to_base_unit(self, value, unit):
        if unit not in self.CONVERSION_FACTORS:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * self.CONVERSION_FACTORS[unit]

    def from_base_unit(self, value_in_liters, target_unit):
        if target_unit not in self.CONVERSION_FACTORS:
            raise ValueError(f"Unsupported unit: {target_unit}")
        factor = self.CONVERSION_FACTORS[target_unit]
        return value_in_liters / factor

    def convert(self, value, source_unit, target_unit):
        liters = self.to_base_unit(value, source_unit)
        return self.from_base_unit(liters, target_unit)

if __name__ == '__main__':
    converter = VolumeConverter()
    gallons_to_liters = converter.to_base_unit(5, 'gallon_us')
    liters_to_pints = converter.from_base_unit(10, 'pint_us')
    cubic_meters_to_gallons = converter.convert(1, 'cubic_meter', 'gallon_us')
    print(gallons_to_liters)
    print(liters_to_pints)
    print(cubic_meters_to_gallons)