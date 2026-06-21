class VolumeConverter:
    FACTORS_TO_LITER = {
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
        'tablespoon_uk': 0.0177581640625,
        'teaspoon_us': 0.00492892159375,
        'teaspoon_uk': 0.005919388203125,
        'cubic_meter': 1000.0,
        'cubic_centimeter': 0.001,
        'cubic_inch': 0.016387064,
        'cubic_foot': 28.316846592,
        'barrel_oil': 158.987294928,
    }

    def __init__(self, value, from_unit, to_unit=None):
        if to_unit is None:
            self.value = value
            self.from_unit = from_unit
            self.to_unit = None
        else:
            self.value = value
            self.from_unit = from_unit
            self.to_unit = to_unit

    def _get_factor(self, unit):
        normalized = unit.lower().strip()
        if normalized in self.FACTORS_TO_LITER:
            return self.FACTORS_TO_LITER[normalized]
        raise ValueError(f"Unsupported unit: {unit}")

    def to_liter(self):
        factor = self._get_factor(self.from_unit)
        return self.value * factor

    def convert(self, to_unit):
        if self.to_unit is not None and to_unit is None:
            target = self.to_unit
        else:
            target = to_unit
        
        if self.value is None or self.from_unit is None or target is None:
            return None

        from_factor = self._get_factor(self.from_unit)
        to_factor = self._get_factor(target)
        
        base_volume = self.value * from_factor
        result = base_volume / to_factor
        
        return result

    def __str__(self):
        if self.to_unit is None:
            return f"{self.value} {self.from_unit} in liters is {self.to_liter()}"
        return f"{self.value} {self.from_unit} is {self.convert(self.to_unit)} {self.to_unit}"

if __name__ == '__main__':
    converter = VolumeConverter(10, 'gallon_us', 'liter')
    print(converter)
    
    direct_conversion = VolumeConverter(10, 'gallon_us')
    liter_value = direct_conversion.to_liter()
    print(f"Direct to liter: {liter_value}")
    
    converter2 = VolumeConverter(5, 'cubic_meter', 'gallon_us')
    print(converter2)
    
    converter3 = VolumeConverter(1, 'liter', 'milliliter')
    print(converter3)