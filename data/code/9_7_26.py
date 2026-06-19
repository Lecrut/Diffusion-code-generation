import unittest

def convert_volume(volume, from_unit, to_unit):
    conversion_factors = {
        'm3_to_cm3': 1e6,
        'cm3_to_m3': 1e-6,
        'l_to_ml': 1000,
        'ml_to_l': 0.001,
        'gal_to_l': 3.78541,
        'l_to_gal': 0.264172
    }
    
    key = f"{from_unit}_to_{to_unit}"
    if key not in conversion_factors:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
    
    return volume * conversion_factors[key]

class TestVolumeConversion(unittest.TestCase):
    def test_m3_to_cm3(self):
        self.assertEqual(convert_volume(1, 'm3', 'cm3'), 1e6)
        self.assertEqual(convert_volume(0, 'm3', 'cm3'), 0)
        self.assertEqual(convert_volume(1.5, 'm3', 'cm3'), 1.5e6)

    def test_cm3_to_m3(self):
        self.assertEqual(convert_volume(1e6, 'cm3', 'm3'), 1)
        self.assertEqual(convert_volume(0, 'cm3', 'm3'), 0)
        self.assertEqual(convert_volume(1.5e6, 'cm3', 'm3'), 1.5)

    def test_l_to_ml(self):
        self.assertEqual(convert_volume(1, 'l', 'ml'), 1000)
        self.assertEqual(convert_volume(0, 'l', 'ml'), 0)
        self.assertEqual(convert_volume(1.5, 'l', 'ml'), 1500)

    def test_ml_to_l(self):
        self.assertEqual(convert_volume(1000, 'ml', 'l'), 1)
        self.assertEqual(convert_volume(0, 'ml', 'l'), 0)
        self.assertEqual(convert_volume(1500, 'ml', 'l'), 1.5)

    def test_gal_to_l(self):
        self.assertEqual(convert_volume(1, 'gal', 'l'), 3.78541)
        self.assertEqual(convert_volume(0, 'gal', 'l'), 0)
        self.assertEqual(convert_volume(2, 'gal', 'l'), 7.57082)

    def test_l_to_gal(self):
        self.assertEqual(convert_volume(3.78541, 'l', 'gal'), 1)
        self.assertEqual(convert_volume(0, 'l', 'gal'), 0)
        self.assertEqual(convert_volume(7.57082, 'l', 'gal'), 2)

    def test_invalid_conversion(self):
        with self.assertRaises(ValueError):
            convert_volume(1, 'm3', 'invalid')

if __name__ == '__main__':
    print(convert_volume(1000, 'ml', 'l'))
    unittest.main(argv=[''], exit=False)