class VolumeConverter:
    def __init__(self):
        self._to_liters = {
            'liter': 1.0,
            'liter_g': 1.0,
            'milliliter': 0.001,
            'milliliter_g': 0.001,
            'millilitre': 0.001,
            'millilitre_g': 0.001,
            'gallon': 3.785411784,
            'gallon_g': 3.785411784,
            'quart': 0.946352946,
            'quart_g': 0.946352946,
            'pint': 0.473176473,
            'pint_g': 0.473176473,
            'cup': 0.2365882365,
            'cup_g': 0.2365882365,
            'fluid_ounce': 0.0295735295625,
            'fluid_ounce_g': 0.0295735295625,
            'fl_oz': 0.0295735295625,
            'fl_oz_g': 0.0295735295625,
        }

    def convert(self, amount, from_unit, to_unit):
        if amount < 0:
            return -abs(amount)
        
        from_key = from_unit.lower().replace(' ', '_')
        to_key = to_unit.lower().replace(' ', '_')
        
        if from_key not in self._to_liters:
            raise ValueError(f"Unsupported from_unit: {from_unit}")
        if to_key not in self._to_liters:
            raise ValueError(f"Unsupported to_unit: {to_unit}")
            
        liters = amount * self._to_liters[from_key]
        result = liters / self._to_liters[to_key]
        return result

if __name__ == '__main__':
    converter = VolumeConverter()
    result = converter.convert(1, 'gallon', 'liter')
    print(result)
    result2 = converter.convert(500, 'milliliter', 'cup')
    print(result2)
    result3 = converter.convert(2, 'liter', 'quart')
    print(result3)
    result4 = converter.convert(100, 'fluid_ounce', 'milliliter')
    print(result4)