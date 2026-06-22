import unittest

def convert_volume(volume, from_unit, to_unit):
    conversion_factors = {'m3_to_cm3': 1000000, 'cm3_to_m3': 1e-06, 'm3_to_liters': 1000, 'liters_to_m3': 0.001, 'cm3_to_liters': 1, 'liters_to_cm3': 1}
    conversion_key = f'{from_unit}_to_{to_unit}'
    if conversion_key not in conversion_factors:
        raise ValueError('Invalid volume conversion')
    converted_volume = volume * conversion_factors[conversion_key]
    return converted_volume

class TestVolumeConversion(unittest.TestCase):

    def test_m3_to_cm3(self):
        self.assertEqual(convert_volume(1, 'm3', 'cm3'), 1000000)

    def test_cm3_to_m3(self):
        self.assertEqual(convert_volume(1000000, 'cm3', 'm3'), 1)

    def test_m3_to_liters(self):
        self.assertEqual(convert_volume(1, 'm3', 'liters'), 1000)

    def test_liters_to_m3(self):
        self.assertEqual(convert_volume(1000, 'liters', 'm3'), 1)

    def test_cm3_to_liters(self):
        self.assertEqual(convert_volume(1, 'cm3', 'liters'), 1)

    def test_liters_to_cm3(self):
        self.assertEqual(convert_volume(1, 'liters', 'cm3'), 1)

    def test_zero_volume(self):
        self.assertEqual(convert_volume(0, 'm3', 'cm3'), 0)

    def test_large_number(self):
        self.assertEqual(convert_volume(999999999, 'm3', 'liters'), 999999999000)
if __name__ == '__main__':
    print('1 m3 to cm3:', convert_volume(1, 'm3', 'cm3'))
    print('1000000 cm3 to m3:', convert_volume(1000000, 'cm3', 'm3'))
    print('0 m3 to cm3:', convert_volume(0, 'm3', 'cm3'))
    print('999999999 m3 to liters:', convert_volume(999999999, 'm3', 'liters'))
    unittest.main(argv=[''], exit=False)