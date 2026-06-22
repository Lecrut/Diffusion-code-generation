class VolumeConverter:
    _factor = {
        'l': 1.0,
        'milliliter': 0.001,
        'milliliter_ml': 0.001,
        'ml': 0.001,
        'liter': 1.0,
        'liter_l': 1.0,
        'gallon_us': 3.785411784,
        'gallon_us_gal': 3.785411784,
        'gallon': 3.785411784,
        'gallon_uk': 4.54609,
        'gallon_uk_gal': 4.54609,
        'cup_us': 0.2365882365,
        'cup_us_cup': 0.2365882365,
        'cup': 0.2365882365,
        'tablespoon_us': 0.0147867648,
        'tablespoon_us_tbsp': 0.0147867648,
        'tablespoon': 0.0147867648,
        'teaspoon_us': 0.0049289216,
        'teaspoon_us_tsp': 0.0049289216,
        'teaspoon': 0.0049289216,
        'cubic_meter': 1000.0,
        'cubic_meter_m3': 1000.0,
        'm3': 1000.0,
        'cubic_centimeter': 0.001,
        'cubic_centimeter_cm3': 0.001,
        'cm3': 0.001,
        'cubic_inch': 0.016387064,
        'cubic_inch_in3': 0.016387064,
        'in3': 0.016387064,
        'cubic_foot': 28.316846592,
        'cubic_foot_ft3': 28.316846592,
        'ft3': 28.316846592,
        'pint_us': 0.473176473,
        'pint_us_pt': 0.473176473,
        'pint': 0.473176473,
        'quart_us': 0.946352946,
        'quart_us_qt': 0.946352946,
        'quart': 0.946352946,
        'fluid_ounce_us': 0.0295735295625,
        'fluid_ounce_us_floz': 0.0295735295625,
        'floz': 0.0295735295625,
    }

    def __init__(self):
        self.conversion_factors = self._factor

    def _to_base(self, value, from_unit):
        factor = self.conversion_factors.get(from_unit)
        if factor is None:
            raise ValueError(f"Unsupported unit: {from_unit}")
        return value * factor

    def _from_base(self, value, to_unit):
        factor = self.conversion_factors.get(to_unit)
        if factor is None:
            raise ValueError(f"Unsupported unit: {to_unit}")
        return value / factor

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        base_value = self._to_base(value, from_unit)
        result = self._from_base(base_value, to_unit)
        return result

if __name__ == '__main__':
    converter = VolumeConverter()
    gallons_to_liters = converter.convert(5, 'gallon_us', 'liter')
    print(f"5 gallons is {gallons_to_liters} liters")
    
    milliliters_to_gallons = converter.convert(1000, 'milliliter', 'gallon_us')
    print(f"1000 milliliters is {milliliters_to_gallons} gallons")
    
    cubic_inches_to_liters = converter.convert(1, 'cubic_inch', 'liter')
    print(f"1 cubic inch is {cubic_inches_to_liters} liters")