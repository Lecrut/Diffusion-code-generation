import unittest

def convert_volume(volume, from_unit, to_unit):
    conversion_factors = {'m3_to_cm3': 10 ** 6, 'cm3_to_m3': 10 ** (-6), 'l_to_ml': 1000, 'ml_to_l': 0.001, 'gal_to_l': 3.78541, 'l_to_gal': 0.264172}
    key = f'{from_unit}_to_{to_unit}'
    if key in conversion_factors:
        return volume * conversion_factors[key]
    else:
        raise ValueError('Unsupported unit conversion')

class TestVolumeConversion(unittest.TestCase):

    def test_zero_volume(self):
        self.assertEqual(convert_volume(0, 'm3', 'cm3'), 0)
        self.assertEqual(convert_volume(0, 'cm3', 'm3'), 0)

    def test_large_numbers(self):
        self.assertEqual(convert_volume(10 ** 6, 'm3', 'cm3'), 10 ** 12)
        self.assertEqual(convert_volume(10 ** 12, 'cm3', 'm3'), 10 ** 6)

    def test_basic_conversion(self):
        self.assertAlmostEqual(convert_volume(1, 'l', 'ml'), 1000)
        self.assertAlmostEqual(convert_volume(1000, 'ml', 'l'), 1)

    def test_gallon_to_liter(self):
        self.assertAlmostEqual(convert_volume(1, 'gal', 'l'), 3.78541)
        self.assertAlmostEqual(convert_volume(3.78541, 'l', 'gal'), 1)
if __name__ == '__main__':
    print(convert_volume(0, 'm3', 'cm3'))
    print(convert_volume(1, 'l', 'ml'))
    print(convert_volume(10 ** 6, 'm3', 'cm3'))
    unittest.main(argv=[''], exit=False)