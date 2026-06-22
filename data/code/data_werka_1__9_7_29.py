import unittest

def convert_volume(volume, from_unit, to_unit):
    conversion_factors = {'m3': {'m3': 1, 'L': 1000}, 'L': {'m3': 0.001, 'L': 1}}
    if from_unit not in conversion_factors or to_unit not in conversion_factors[from_unit]:
        raise ValueError('Invalid unit conversion')
    return volume * conversion_factors[from_unit][to_unit]

class TestVolumeConversion(unittest.TestCase):

    def test_convert_m3_to_L(self):
        self.assertEqual(convert_volume(1, 'm3', 'L'), 1000)

    def test_convert_L_to_m3(self):
        self.assertEqual(convert_volume(1000, 'L', 'm3'), 1)

    def test_convert_zero_volume(self):
        self.assertEqual(convert_volume(0, 'm3', 'L'), 0)
        self.assertEqual(convert_volume(0, 'L', 'm3'), 0)

    def test_convert_large_numbers(self):
        self.assertEqual(convert_volume(999999999, 'm3', 'L'), 999999999000)
        self.assertEqual(convert_volume(999999999000, 'L', 'm3'), 999999999)

    def test_invalid_conversion(self):
        with self.assertRaises(ValueError):
            convert_volume(1, 'm3', 'km')
        with self.assertRaises(ValueError):
            convert_volume(1, 'kg', 'L')
if __name__ == '__main__':
    print(convert_volume(2, 'm3', 'L'))
    print(convert_volume(500, 'L', 'm3'))
    unittest.main(argv=[''], exit=False)