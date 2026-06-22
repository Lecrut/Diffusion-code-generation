import unittest
import math

def convert_volume(value, from_unit, to_unit):
    factors = {
        'liters': 1.0,
        'milliliters': 0.001,
        'gallons': 3.78541,
        'quarts': 0.946353,
        'pints': 0.473176,
        'cups': 0.236588,
        'fluid_ounces': 0.0295735,
        'cubic_meters': 1000.0,
        'cubic_inches': 0.0163871,
    }
    
    if from_unit not in factors or to_unit not in factors:
        raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")
    
    value_in_liters = value * factors[from_unit]
    result = value_in_liters / factors[to_unit]
    
    return result

class TestVolumeConversion(unittest.TestCase):
    def test_liters_to_liters(self):
        self.assertEqual(convert_volume(10, 'liters', 'liters'), 10.0)
    
    def test_liters_to_milliliters(self):
        self.assertAlmostEqual(convert_volume(1, 'liters', 'milliliters'), 1000.0)
    
    def test_milliliters_to_liters(self):
        self.assertAlmostEqual(convert_volume(500, 'milliliters', 'liters'), 0.5)
    
    def test_gallons_to_liters(self):
        self.assertAlmostEqual(convert_volume(1, 'gallons', 'liters'), 3.78541, places=5)
    
    def test_liters_to_gallons(self):
        self.assertAlmostEqual(convert_volume(3.78541, 'liters', 'gallons'), 1.0, places=5)
    
    def test_zero_volume(self):
        self.assertEqual(convert_volume(0, 'liters', 'gallons'), 0.0)
        self.assertEqual(convert_volume(0, 'gallons', 'milliliters'), 0.0)
    
    def test_large_number(self):
        large_val = 1_000_000
        result = convert_volume(large_val, 'cubic_meters', 'liters')
        self.assertEqual(result, 1_000_000_000.0)
    
    def test_invalid_unit_from(self):
        with self.assertRaises(ValueError):
            convert_volume(10, 'unknown', 'liters')
    
    def test_invalid_unit_to(self):
        with self.assertRaises(ValueError):
            convert_volume(10, 'liters', 'unknown')
    
    def test_cubic_meters_to_liters(self):
        self.assertEqual(convert_volume(1, 'cubic_meters', 'liters'), 1000.0)
    
    def test_quarts_to_pints(self):
        self.assertAlmostEqual(convert_volume(1, 'quarts', 'pints'), 2.0)

if __name__ == '__main__':
    print(convert_volume(1, 'liters', 'milliliters'))
    print(convert_volume(5, 'gallons', 'liters'))
    print(convert_volume(0, 'liters', 'gallons'))
    print(convert_volume(1000000, 'cubic_meters', 'liters'))
    print(convert_volume(32, 'cups', 'pints'))
    unittest.main()