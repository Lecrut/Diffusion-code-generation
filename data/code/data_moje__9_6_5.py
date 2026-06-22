class VolumeConverter:
    def __init__(self):
        self.units = {
            'L': 1.0,
            'ml': 0.001,
            'm3': 1000.0,
            'gal': 3.785411784,
            'qt': 0.946352946,
            'pt': 0.473176473,
            'fl_oz': 0.0295735296,
            'cubic_meter': 1000.0,
            'cubic_foot': 28.316846592,
            'liter': 1.0,
            'gallon': 3.785411784,
            'quart': 0.946352946,
            'pint': 0.473176473,
            'cup': 0.2365882365,
            'tablespoon': 0.0147867648,
            'teaspoon': 0.0049289216
        }
        self.synonyms = {
            'm^3': 'm3',
            'cubic meters': 'm3',
            'l': 'L',
            'liters': 'L',
            'gal': 'gallon',
            'gallons': 'gallon',
            'qt': 'quart',
            'quarts': 'quart',
            'pt': 'pint',
            'pints': 'pint',
            'oz': 'fl_oz',
            'cups': 'cup',
            'tbsp': 'tablespoon',
            'tsp': 'teaspoon'
        }

    def _normalize(self, unit):
        if unit in self.synonyms:
            return self.synonyms[unit]
        if unit in self.units:
            return unit
        raise ValueError(f"Unknown unit: {unit}")

    def convert(self, value, from_unit, to_unit):
        from_key = self._normalize(from_unit)
        to_key = self._normalize(to_unit)
        if from_key not in self.units or to_key not in self.units:
            raise ValueError("Unit not found in dictionary")
        base_value = value * self.units[from_key]
        result = base_value / self.units[to_key]
        return result

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_liters = 5
    sample_m3 = 2
    sample_gallons = 10
    result1 = converter.convert(sample_liters, 'L', 'ml')
    result2 = converter.convert(sample_m3, 'm^3', 'gal')
    result3 = converter.convert(sample_gallons, 'gallon', 'quart')
    print(result1)
    print(result2)
    print(result3)