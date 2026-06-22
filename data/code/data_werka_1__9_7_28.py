import unittest

def convert_volume(volume, from_unit, to_unit):
    conversion_factors = {'m3': {'m3': 1, 'cm3': 1000000, 'liters': 1000}, 'cm3': {'m3': 1e-06, 'cm3': 1, 'liters': 1}, 'liters': {'m3': 0.001, 'cm3': 1, 'liters': 1}}
    if from_unit not in conversion_factors or to_unit not in conversion_factors[from_unit]:
        raise ValueError('Invalid unit conversion')
    return volume * conversion_factors[from_unit][to_unit]

class TestVolumeConversion(unittest.TestCase):

    def test_zero_volume(self):
        self.assertEqual(convert_volume(0, 'm3', 'cm3'), 0)
        self.assertEqual(convert_volume(0, 'cm3', 'liters'), 0)
        self.assertEqual(convert_volume(0, 'liters', 'm3'), 0)

    def test_large_numbers(self):
        self.assertEqual(convert_volume(1000000.0, 'm3', 'cm3'), 1000000000000.0)
        self.assertEqual(convert_volume(1000000000.0, 'cm3', 'liters'), 1000000.0)
        self.assertEqual(convert_volume(1000.0, 'liters', 'm3'), 1)

    def test_same_unit(self):
        self.assertEqual(convert_volume(5, 'm3', 'm3'), 5)
        self.assertEqual(convert_volume(100, 'cm3', 'cm3'), 100)
        self.assertEqual(convert_volume(2000, 'liters', 'liters'), 2000)

    def test_invalid_conversion(self):
        with self.assertRaises(ValueError):
            convert_volume(1, 'm3', 'gallons')
        with self.assertRaises(ValueError):
            convert_volume(1, 'kg', 'liters')
if __name__ == '__main__':
    print(convert_volume(5, 'm3', 'cm3'))
    print(convert_volume(1000, 'cm3', 'liters'))
    print(convert_volume(2, 'liters', 'm3'))
    unittest.main(argv=[''], exit=False)