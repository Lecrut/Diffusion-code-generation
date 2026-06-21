import math

VOLUME_UNITS = {
    'L': 1.0,
    'ml': 0.001,
    'm3': 1000.0,
    'gal': 3.78541,
    'qt': 0.946353,
    'pt': 0.473176,
    'cup': 0.236588,
    'floz': 0.0295735,
    'tbsp': 0.0147868,
    'tsp': 0.00492892
}

class VolumeConverter:
    def __init__(self, units=None):
        if units is None:
            self.units = VOLUME_UNITS.copy()
        else:
            self.units = units

    def convert(self, amount, from_unit, to_unit):
        if from_unit not in self.units:
            raise KeyError(f"Unknown unit: {from_unit}")
        if to_unit not in self.units:
            raise KeyError(f"Unknown unit: {to_unit}")
        
        base_amount = amount * self.units[from_unit]
        result = base_amount / self.units[to_unit]
        return result

if __name__ == '__main__':
    converter = VolumeConverter()
    
    result_l_to_ml = converter.convert(1, 'L', 'ml')
    print(f"1 L = {result_l_to_ml} ml")
    
    result_m3_to_gal = converter.convert(1, 'm3', 'gal')
    print(f"1 m³ = {result_m3_to_gal} gal")
    
    result_gal_to_l = converter.convert(1, 'gal', 'L')
    print(f"1 gal = {result_gal_to_l} L")