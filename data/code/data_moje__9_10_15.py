class VolumeConverter:
    _to_base = {
        'liter': 1.0,
        'milliliter': 0.001,
        'millilitre': 0.001,
        'cubic_meter': 1000.0,
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
        'teaspoon_uk': 0.0059193884166667,
        'cubic_foot': 28.316846592,
        'cubic_inch': 0.016387064,
        'barrel_oil': 158.987294928,
        'barrel_us': 0.1192404712,
    }

    def __init__(self):
        self._cache = {}

    def to_base(self, value, unit):
        unit_lower = unit.lower().strip()
        if unit_lower not in self._to_base:
            raise ValueError(f'Unit {unit} is not supported.')
        
        key = (unit_lower, value)
        if key in self._cache:
            return self._cache[key]
        
        factor = self._to_base[unit_lower]
        result = value * factor
        self._cache[key] = result
        return result

    def from_base(self, value_in_liters, unit):
        unit_lower = unit.lower().strip()
        if unit_lower not in self._to_base:
            raise ValueError(f'Unit {unit} is not supported.')
        
        key = (unit_lower, value_in_liters)
        if key in self._cache:
            return self._cache[key]
        
        factor = self._to_base[unit_lower]
        if factor == 0:
            return 0.0
        
        result = value_in_liters / factor
        self._cache[key] = result
        return result

    def convert(self, value, from_unit, to_unit):
        base_value = self.to_base(value, from_unit)
        return self.from_base(base_value, to_unit)

if __name__ == '__main__':
    converter = VolumeConverter()
    
    gallons = 1.0
    result_ml = converter.convert(gallons, 'gallon_us', 'milliliter')
    print(f'{gallons} gallon_us = {result_ml} milliliter')
    
    result_cubic_meter = converter.convert(5000, 'liter', 'cubic_meter')
    print(f'{5000} liter = {result_cubic_meter} cubic_meter')
    
    result_gallons = converter.convert(100, 'gallon_uk', 'gallon_us')
    print(f'{100} gallon_uk = {result_gallons} gallon_us')
    
    result_liters = converter.convert(1000, 'cubic_inch', 'liter')
    print(f'{1000} cubic_inch = {result_liters} liter')