class VolumeConverter:
    _LITERS_TO_UNIT = {
        'liter': 1.0,
        'milliliter': 0.001,
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
        'tablespoon_uk': 0.0177581640625,
        'teaspoon_us': 0.00492892159375,
        'teaspoon_uk': 0.0059193946875,
        'cubic_meter': 1000.0,
        'cubic_foot': 28.316846592,
        'cubic_inch': 0.016387064,
    }

    def to_base(self, value, from_unit):
        from_unit_lower = from_unit.lower()
        if from_unit_lower not in self._LITERS_TO_UNIT:
            raise ValueError(f"Unsupported unit: {from_unit}")
        liters = value * self._LITERS_TO_UNIT[from_unit_lower]
        return liters

    def from_base(self, value, to_unit):
        to_unit_lower = to_unit.lower()
        if to_unit_lower not in self._LITERS_TO_UNIT:
            raise ValueError(f"Unsupported unit: {to_unit}")
        target_value = value / self._LITERS_TO_UNIT[to_unit_lower]
        return target_value

    def convert(self, value, from_unit, to_unit):
        base_value = self.to_base(value, from_unit)
        result = self.from_base(base_value, to_unit)
        return result

if __name__ == '__main__':
    converter = VolumeConverter()
    liters_result = converter.to_base(5, 'gallon_us')
    print(liters_result)
    
    gallons_result = converter.from_base(10, 'gallon_us')
    print(gallons_result)
    
    direct_result = converter.convert(1, 'cubic_meter', 'gallon_us')
    print(direct_result)