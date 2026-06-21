class VolumeConverter:
    def __init__(self):
        self._liters_per_unit = {
            'L': 1.0,
            'mL': 0.001,
            'gal': 3.785411784,
            'qt': 0.946352946,
            'pt': 0.473176473,
            'cup': 0.23659116,
            'floz': 0.02957353,
            'Oz': 0.02957353,
            'fl_oz': 0.02957353
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self._liters_per_unit:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self._liters_per_unit:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        liters = value * self._liters_per_unit[from_unit]
        converted_value = liters / self._liters_per_unit[to_unit]
        return converted_value

    def get_units(self):
        return list(self._liters_per_unit.keys())

if __name__ == '__main__':
    converter = VolumeConverter()
    result = converter.convert(1, 'L', 'floz')
    print(result)
    
    result2 = converter.convert(1000, 'mL', 'gal')
    print(result2)
    
    result3 = converter.convert(1, 'gal', 'cup')
    print(result3)