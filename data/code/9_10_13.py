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
        'cubic_inch': 0.016387064,
        'cubic_foot': 28.316846592,
        'cubic_yard': 764.554857984,
        'liter_metric': 1.0,
        'milliliter_metric': 0.001,
        'liter_uk': 1.0,
        'gallon_uk': 4.54609,
        'quart_uk': 1.1365225,
        'pint_uk': 0.56826125,
        'fluid_ounce_uk': 0.0284130625,
    }

    def __init__(self):
        self._base_unit = 'liter'

    def _get_factor(self, unit):
        unit_lower = unit.lower()
        if unit_lower in self.LITERS_PER_UNIT:
            return self.LITERS_PER_UNIT[unit_lower]
        raise ValueError(f"Unsupported unit: {unit}")

    def to_base_unit(self, value, from_unit):
        factor = self._get_factor(from_unit)
        return value * factor

    def from_base_unit(self, value, to_unit):
        factor = self._get_factor(to_unit)
        return value / factor

    def convert(self, value, from_unit, to_unit):
        if from_unit.lower() == to_unit.lower():
            return value
        base_value = self.to_base_unit(value, from_unit)
        return self.from_base_unit(base_value, to_unit)

if __name__ == '__main__':
    converter = VolumeConverter()
    gallons_to_liters = converter.to_base_unit(5.0, 'gallon_us')
    print(gallons_to_liters)
    liters_to_cups = converter.convert(1.0, 'liter', 'cup_us')
    print(liters_to_cups)
    cubic_meters_to_cubic_feet = converter.convert(1.0, 'cubic_meter', 'cubic_foot')
    print(cubic_meters_to_cubic_feet)
    uk_gallons_to_liter = converter.to_base_unit(2.5, 'gallon_uk')
    print(uk_gallons_to_liter)
    us_pints_to_cubic_inches = converter.convert(10.0, 'pint_us', 'cubic_inch')
    print(us_pints_to_cubic_inches)