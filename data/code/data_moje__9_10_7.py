class VolumeConverter:
    def __init__(self):
        self._units_to_liters = {
            'liter': 1.0,
            'litre': 1.0,
            'milliliter': 0.001,
            'millilitre': 0.001,
            'gallon_us': 3.785411784,
            'gallon_uk': 4.54609,
            'quart_us': 0.946352946,
            'quart_uk': 1.1365225,
            'pint_us': 0.473176473,
            'pint_uk': 0.56826125,
            'cup_us': 0.2365882365,
            'cup_uk': 0.284130625,
            'fluid_ounce_us': 0.0295735295625,
            'fluid_ounce_uk': 0.0284130625,
            'tablespoon_us': 0.01478676478125,
            'teaspoon_us': 0.00492892159375,
            'cubic_meter': 1000.0,
            'cubic_centimeter': 0.001,
            'cubic_millimeter': 0.000001,
            'cubic_inch': 0.016387064,
            'cubic_foot': 28.316846592,
            'cubic_yard': 764.554857984,
            'barrel_oil': 158.987294928,
            'barrel_us_liquid': 0.119240471196,
            'hogshead_us': 0.238480942392,
        }
        self._valid_units = set(self._units_to_liters.keys())

    def to_base_unit(self, value, unit):
        lower_unit = unit.lower()
        if lower_unit not in self._valid_units:
            raise ValueError(f"Unsupported unit: {unit}")
        liters = value * self._units_to_liters[lower_unit]
        return liters

    def from_base_unit(self, value, target_unit):
        target_lower = target_unit.lower()
        if target_lower not in self._valid_units:
            raise ValueError(f"Unsupported unit: {target_unit}")
        conversion_factor = self._units_to_liters[target_lower]
        if conversion_factor == 0:
            raise ValueError("Conversion factor cannot be zero")
        result = value / conversion_factor
        return result

    def convert(self, value, from_unit, to_unit):
        liters = self.to_base_unit(value, from_unit)
        result = self.from_base_unit(liters, to_unit)
        return result

if __name__ == '__main__':
    converter = VolumeConverter()
    liters_value = converter.to_base_unit(5, 'gallon_us')
    print(f"5 US gallons in liters: {liters_value}")
    
    gallons_back = converter.from_base_unit(18.92705892, 'gallon_us')
    print(f"18.92705892 liters in US gallons: {gallons_back}")
    
    direct_conversion = converter.convert(1, 'cubic_meter', 'liter')
    print(f"1 cubic meter in liters: {direct_conversion}")