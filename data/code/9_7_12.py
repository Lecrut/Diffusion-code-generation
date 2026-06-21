import unittest
import math

def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        ('ml', 'ml'): 1.0,
        ('ml', 'l'): 0.001,
        ('ml', 'gallon'): 0.000264172,
        ('ml', 'cup'): 0.00422675,
        ('l', 'ml'): 1000.0,
        ('l', 'l'): 1.0,
        ('l', 'gallon'): 0.264172,
        ('l', 'cup'): 4.22675,
        ('gallon', 'ml'): 3785.41,
        ('gallon', 'l'): 3.78541,
        ('gallon', 'gallon'): 1.0,
        ('gallon', 'cup'): 16.0,
        ('cup', 'ml'): 236.588,
        ('cup', 'l'): 0.236588,
        ('cup', 'gallon'): 0.0625,
        ('cup', 'cup'): 1.0,
    }
    key = (from_unit, to_unit)
    if key not in conversion_factors:
        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")
    return value * conversion_factors[key]

class TestVolumeConversion(unittest.TestCase):
    def test_ml_to_ml(self):
        self.assertAlmostEqual(convert_volume(100, 'ml', 'ml'), 100.0)

    def test_ml_to_l(self):
        self.assertAlmostEqual(convert_volume(1000, 'ml', 'l'), 1.0)

    def test_l_to_ml(self):
        self.assertAlmostEqual(convert_volume(1, 'l', 'ml'), 1000.0)

    def test_l_to_gallon(self):
        self.assertAlmostEqual(convert_volume(1, 'l', 'gallon'), 0.264172, places=5)

    def test_gallon_to_l(self):
        self.assertAlmostEqual(convert_volume(1, 'gallon', 'l'), 3.78541, places=5)

    def test_cup_to_ml(self):
        self.assertAlmostEqual(convert_volume(1, 'cup', 'ml'), 236.588, places=5)

    def test_zero_volume(self):
        self.assertEqual(convert_volume(0, 'ml', 'l'), 0.0)

    def test_large_number(self):
        result = convert_volume(1e10, 'ml', 'l')
        self.assertAlmostEqual(result, 1e7, delta=1.0)

    def test_negative_volume_raises(self):
        with self.assertRaises(ValueError):
            convert_volume(-100, 'ml', 'l')

    def test_unsupported_unit_raises(self):
        with self.assertRaises(ValueError):
            convert_volume(100, 'ml', 'pint')

if __name__ == '__main__':
    test_case = TestVolumeConversion()
    test_case.test_ml_to_ml()
    test_case.test_ml_to_l()
    test_case.test_l_to_ml()
    test_case.test_l_to_gallon()
    test_case.test_gallon_to_l()
    test_case.test_cup_to_ml()
    test_case.test_zero_volume()
    test_case.test_large_number()
    print(convert_volume(1000, 'ml', 'l'))
    print(convert_volume(0, 'ml', 'gallon'))
    print(convert_volume(1e12, 'ml', 'gallon'))