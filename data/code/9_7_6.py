import unittest
import math

def convert_volume(value, from_unit, to_unit):
    conversions = {
        ('ml', 'l'): 0.001,
        ('ml', 'gal'): 0.000264172,
        ('ml', 'tsp'): 0.202884,
        ('ml', 'tbsp'): 0.067628,
        ('ml', 'cup'): 0.00422675,
        ('ml', 'floz'): 0.033814,
        ('l', 'ml'): 1000.0,
        ('l', 'gal'): 0.264172,
        ('l', 'tsp'): 202.884,
        ('l', 'tbsp'): 67.628,
        ('l', 'cup'): 4.22675,
        ('l', 'floz'): 33.814,
        ('gal', 'ml'): 3785.41,
        ('gal', 'l'): 3.78541,
        ('gal', 'tsp'): 768.0,
        ('gal', 'tbsp'): 256.0,
        ('gal', 'cup'): 16.0,
        ('gal', 'floz'): 128.0,
        ('tsp', 'ml'): 4.92892,
        ('tsp', 'l'): 0.00492892,
        ('tsp', 'gal'): 0.00130208,
        ('tsp', 'tbsp'): 0.166667,
        ('tsp', 'cup'): 0.0208333,
        ('tsp', 'floz'): 0.166667,
        ('tbsp', 'ml'): 14.7868,
        ('tbsp', 'l'): 0.0147868,
        ('tbsp', 'gal'): 0.00390625,
        ('tbsp', 'tsp'): 3.0,
        ('tbsp', 'cup'): 0.0625,
        ('tbsp', 'floz'): 0.5,
        ('cup', 'ml'): 236.588,
        ('cup', 'l'): 0.236588,
        ('cup', 'gal'): 0.0625,
        ('cup', 'tsp'): 48.0,
        ('cup', 'tbsp'): 16.0,
        ('cup', 'floz'): 8.0,
        ('floz', 'ml'): 29.5735,
        ('floz', 'l'): 0.0295735,
        ('floz', 'gal'): 0.0078125,
        ('floz', 'tsp'): 6.0,
        ('floz', 'tbsp'): 2.0,
        ('floz', 'cup'): 0.125,
    }
    if from_unit == to_unit:
        return value
    if (from_unit, to_unit) not in conversions:
        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")
    if value < 0:
        raise ValueError("Volume cannot be negative")
    return value * conversions[(from_unit, to_unit)]

class TestVolumeConversion(unittest.TestCase):
    def test_identity_conversion(self):
        self.assertAlmostEqual(convert_volume(5.0, 'l', 'l'), 5.0)
        self.assertAlmostEqual(convert_volume(10.0, 'ml', 'ml'), 10.0)

    def test_zero_volume(self):
        self.assertAlmostEqual(convert_volume(0.0, 'l', 'gal'), 0.0)
        self.assertAlmostEqual(convert_volume(0.0, 'ml', 'tsp'), 0.0)

    def test_large_numbers(self):
        large_val = 1e10
        result = convert_volume(large_val, 'l', 'ml')
        self.assertAlmostEqual(result, large_val * 1000.0)

    def test_negative_volume(self):
        with self.assertRaises(ValueError):
            convert_volume(-1.0, 'l', 'ml')

    def test_unsupported_conversion(self):
        with self.assertRaises(ValueError):
            convert_volume(1.0, 'gallons', 'liters')
        with self.assertRaises(ValueError):
            convert_volume(1.0, 'l', 'ounces')

    def test_precise_conversion_l_to_ml(self):
        self.assertAlmostEqual(convert_volume(1.0, 'l', 'ml'), 1000.0)

    def test_precise_conversion_gal_to_l(self):
        self.assertAlmostEqual(convert_volume(1.0, 'gal', 'l'), 3.78541, places=4)

    def test_chain_conversion_equivalence(self):
        val = 100.0
        direct = convert_volume(val, 'l', 'tsp')
        via_ml = convert_volume(convert_volume(val, 'l', 'ml'), 'ml', 'tsp')
        self.assertAlmostEqual(direct, via_ml, places=4)

    def test_small_positive_volume(self):
        small_val = 1e-9
        result = convert_volume(small_val, 'ml', 'l')
        self.assertAlmostEqual(result, small_val * 0.001)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)