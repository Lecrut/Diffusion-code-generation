import unittest
from typing import Union

class VolumeConverter:
    def __init__(self):
        self.units = {
            'liter': 1.0,
            'milliliter': 0.001,
            'gallon': 3.78541,
            'quart': 0.946353,
            'pint': 0.473176,
            'cup': 0.236588,
            'fluid_ounce': 0.0295735,
            'cubic_meter': 1000.0,
            'cubic_centimeter': 0.001,
            'cubic_inch': 0.0163871,
            'cubic_foot': 28.3168
        }

    def convert(self, value: Union[int, float], from_unit: str, to_unit: str) -> float:
        if from_unit not in self.units:
            raise ValueError(f"Unknown source unit: {from_unit}")
        if to_unit not in self.units:
            raise ValueError(f"Unknown target unit: {to_unit}")
        
        base_value = value * self.units[from_unit]
        result = base_value / self.units[to_unit]
        return result

    def get_supported_units(self):
        return list(self.units.keys())

def convert_volume(value: Union[int, float], from_unit: str, to_unit: str) -> float:
    converter = VolumeConverter()
    return converter.convert(value, from_unit, to_unit)

class TestVolumeConverter(unittest.TestCase):
    def test_liters_to_milliliters(self):
        self.assertAlmostEqual(convert_volume(1, 'liter', 'milliliter'), 1000.0)

    def test_milliliters_to_liters(self):
        self.assertAlmostEqual(convert_volume(1000, 'milliliter', 'liter'), 1.0)

    def test_gallons_to_liters(self):
        self.assertAlmostEqual(convert_volume(1, 'gallon', 'liter'), 3.78541, places=5)

    def test_liters_to_gallons(self):
        self.assertAlmostEqual(convert_volume(3.78541, 'liter', 'gallon'), 1.0, places=5)

    def test_quarts_to_liters(self):
        self.assertAlmostEqual(convert_volume(4, 'quart', 'liter'), 3.78541, places=5)

    def test_pints_to_liters(self):
        self.assertAlmostEqual(convert_volume(2, 'pint', 'liter'), 0.946353, places=5)

    def test_cups_to_liters(self):
        self.assertAlmostEqual(convert_volume(4, 'cup', 'liter'), 0.946353, places=5)

    def test_fluid_ounces_to_liters(self):
        self.assertAlmostEqual(convert_volume(33.814, 'fluid_ounce', 'liter'), 1.0, places=3)

    def test_cubic_meters_to_liters(self):
        self.assertAlmostEqual(convert_volume(1, 'cubic_meter', 'liter'), 1000.0)

    def test_cubic_centimeters_to_liters(self):
        self.assertAlmostEqual(convert_volume(1000, 'cubic_centimeter', 'liter'), 1.0)

    def test_cubic_inches_to_liters(self):
        self.assertAlmostEqual(convert_volume(61.0237, 'cubic_inch', 'liter'), 1.0, places=3)

    def test_cubic_feet_to_liters(self):
        self.assertAlmostEqual(convert_volume(1, 'cubic_foot', 'liter'), 28.3168, places=4)

    def test_zero_volume(self):
        self.assertAlmostEqual(convert_volume(0, 'liter', 'gallon'), 0.0)

    def test_zero_from_different_unit(self):
        self.assertAlmostEqual(convert_volume(0, 'milliliter', 'quart'), 0.0)

    def test_large_value_liters_to_gallons(self):
        result = convert_volume(1000000, 'liter', 'gallon')
        self.assertGreater(result, 0)

    def test_large_value_gallons_to_liters(self):
        result = convert_volume(1000000, 'gallon', 'liter')
        self.assertGreater(result, 0)

    def test_negative_volume(self):
        self.assertAlmostEqual(convert_volume(-1, 'liter', 'gallon'), -0.264172, places=6)

    def test_invalid_from_unit(self):
        with self.assertRaises(ValueError):
            convert_volume(1, 'invalid_unit', 'liter')

    def test_invalid_to_unit(self):
        with self.assertRaises(ValueError):
            convert_volume(1, 'liter', 'invalid_unit')

    def test_same_unit_conversion(self):
        self.assertAlmostEqual(convert_volume(5.5, 'liter', 'liter'), 5.5)

    def test_supported_units_list(self):
        converter = VolumeConverter()
        units = converter.get_supported_units()
        self.assertIn('liter', units)
        self.assertIn('gallon', units)

def run_main():
    c = VolumeConverter()
    val = c.convert(10, 'liter', 'gallon')
    print(val)

if __name__ == '__main__':
    run_main()
    unittest.main()