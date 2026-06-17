import math
from typing import Union
class UnitConverter:
    def __init__(self):
        self.rates = {
            'meters': {'factor': 1},
            'kilometers': {'factor': 0.001, 'base': 'meters'},
            'centimeters': {'factor': 100, 'base': 'meters'},
            'feet': {'factor': 3.28084, 'base': 'meters'},
            'yards': {'factor': 1.09361, 'base': 'meters'},
            'inches': {'factor': 39.3701, 'base': 'meters'}
        }
    def convert(self, value: Union[int, float], from_unit: str, to_unit: str) -> Union[int, float]:
        if not isinstance(value, (int, float)):
            raise TypeError("Length must be an integer or float")
        unit_lower = from_unit.lower()
        target_lower = to_unit.lower()
        if unit_lower not in self.rates or target_lower not in self.rates:
            available_units = ', '.join(self.rates.keys())
            print(f"Error: Invalid units. Available units are {available_units}")
            return None
        source_info = self.rates[unit_lower]
        target_info = self.rates[target_lower]
        if value == 0 or (isinstance(value, float) and math.isclose(value, 0)):
            print("Warning: Zero length provided. Result is zero regardless of units.")
        if value < 0:
            print("Warning: Negative length provided. Result will be negative.")
        intermediate = value * source_info['factor']
        result = intermediate / target_info['factor']
        return round(result, 6)
if __name__ == '__main__':
    converter = UnitConverter()
    print("Test 1:", converter.convert(50.5, 'meters', 'feet'))
    print("Test 2:", converter.convert(0, 'kilometers', 'inches'))
    print("Test 3:", converter.convert(-10, 'meters', 'centimeters'))
    try:
        result = converter.convert(5, 'invalid_unit', 'feet')
        if result is None:
            print("Test 4 handled invalid input gracefully")
    except Exception as e:
        pass
    converter.rates['custom_unit'] = {'factor': 2}
    print("Test 5:", converter.convert(10, 'meters', 'custom_unit'))