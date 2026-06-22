import unittest
import math

class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            'ml': 0.001,
            'l': 1.0,
            'gal': 3.78541,
            'qt': 0.946353,
            'pt': 0.473176,
            'cup': 0.236588,
            'tbsp': 0.0147868,
            'tsp': 0.00492892
        }

    def convert(self, volume, from_unit, to_unit):
        if volume < 0:
            raise ValueError("Volume cannot be negative")
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {from_unit}")
        if to_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {to_unit}")
        
        volume_in_liters = volume * self.conversion_factors[from_unit]
        converted_volume = volume_in_liters / self.conversion_factors[to_unit]
        
        return converted_volume

class TestVolumeConverter(unittest.TestCase):
    def setUp(self):
        self.converter = VolumeConverter()

    def test_zero_volume(self):
        result = self.converter.convert(0, 'l', 'ml')
        self.assertEqual(result, 0.0)

    def test_negative_volume(self):
        with self.assertRaises(ValueError):
            self.converter.convert(-1, 'l', 'ml')

    def test_invalid_from_unit(self):
        with self.assertRaises(ValueError):
            self.converter.convert(1, 'invalid', 'ml')

    def test_invalid_to_unit(self):
        with self.assertRaises(ValueError):
            self.converter.convert(1, 'l', 'invalid')

    def test_large_volume(self):
        result = self.converter.convert(1e10, 'ml', 'l')
        expected = 1e7
        self.assertAlmostEqual(result, expected, places=2)

    def test_small_volume(self):
        result = self.converter.convert(0.000001, 'ml', 'l')
        expected = 1e-9
        self.assertAlmostEqual(result, expected, places=12)

    def test_same_unit_conversion(self):
        result = self.converter.convert(5, 'l', 'l')
        self.assertEqual(result, 5.0)

    def test_ml_to_gal(self):
        result = self.converter.convert(1000, 'ml', 'gal')
        expected = 1.0 / 3.78541
        self.assertAlmostEqual(result, expected, places=5)

    def test_gal_to_ml(self):
        result = self.converter.convert(1, 'gal', 'ml')
        expected = 3785.41
        self.assertAlmostEqual(result, expected, places=2)

    def test_precision_check(self):
        result = self.converter.convert(1, 'l', 'tsp')
        expected = 1 / 0.00492892
        self.assertAlmostEqual(result, expected, places=4)

if __name__ == '__main__':
    converter = VolumeConverter()
    
    print(converter.convert(0, 'l', 'ml'))
    print(converter.convert(1000, 'ml', 'l'))
    print(converter.convert(1, 'gal', 'l'))
    print(converter.convert(5, 'l', 'ml'))
    print(converter.convert(1e6, 'ml', 'gal'))
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVolumeConverter)
    runner = unittest.TextTestRunner(verbosity=0)
    runner.run(suite)