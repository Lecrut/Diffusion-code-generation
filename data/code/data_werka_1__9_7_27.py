import unittest

def convert_volume(volume, from_unit, to_unit):
    conversion_factors = {'m3_to_cm3': 1000000.0, 'cm3_to_m3': 1e-06, 'm3_to_liters': 1000, 'liters_to_m3': 0.001, 'cm3_to_liters': 1, 'liters_to_cm3': 1}
    key = f'{from_unit}_to_{to_unit}'
    if key not in conversion_factors:
        raise ValueError('Unsupported conversion')
    return volume * conversion_factors[key]

class TestVolumeConversion(unittest.TestCase):

    def test_m3_to_cm3(self):
        self.assertEqual(convert_volume(1, 'm3', 'cm3'), 1000000.0)
        self.assertEqual(convert_volume(0, 'm3', 'cm3'), 0)
        self.assertEqual(convert_volume(1.5, 'm3', 'cm3'), 1500000.0)

    def test_cm3_to_m3(self):
        self.assertEqual(convert_volume(1000000.0, 'cm3', 'm3'), 1)
        self.assertEqual(convert_volume(0, 'cm3', 'm3'), 0)
        self.assertEqual(convert_volume(1500000.0, 'cm3', 'm3'), 1.5)

    def test_m3_to_liters(self):
        self.assertEqual(convert_volume(1, 'm3', 'liters'), 1000)
        self.assertEqual(convert_volume(0, 'm3', 'liters'), 0)
        self.assertEqual(convert_volume(1.5, 'm3', 'liters'), 1500)

    def test_liters_to_m3(self):
        self.assertEqual(convert_volume(1000, 'liters', 'm3'), 1)
        self.assertEqual(convert_volume(0, 'liters', 'm3'), 0)
        self.assertEqual(convert_volume(1500, 'liters', 'm3'), 1.5)

    def test_cm3_to_liters(self):
        self.assertEqual(convert_volume(1, 'cm3', 'liters'), 1)
        self.assertEqual(convert_volume(0, 'cm3', 'liters'), 0)
        self.assertEqual(convert_volume(1000, 'cm3', 'liters'), 1)

    def test_liters_to_cm3(self):
        self.assertEqual(convert_volume(1, 'liters', 'cm3'), 1)
        self.assertEqual(convert_volume(0, 'liters', 'cm3'), 0)
        self.assertEqual(convert_volume(1000, 'liters', 'cm3'), 1)

    def test_invalid_conversion(self):
        with self.assertRaises(ValueError):
            convert_volume(1, 'm3', 'km3')
if __name__ == '__main__':
    print(convert_volume(2, 'm3', 'cm3'))
    print(convert_volume(500, 'liters', 'm3'))
    unittest.main(argv=[''], exit=False)