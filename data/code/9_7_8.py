import unittest

class VolumeConverter:
    def convert(self, volume: float, from_unit: str, to_unit: str) -> float:
        factors = {
            ('liter', 'milliliter'): 1000.0,
            ('liter', 'gallon'): 0.264172,
            ('liter', 'cup'): 4.22675,
            ('milliliter', 'liter'): 0.001,
            ('milliliter', 'gallon'): 0.000264172,
            ('milliliter', 'cup'): 0.00422675,
            ('gallon', 'liter'): 3.78541,
            ('gallon', 'milliliter'): 3785.41,
            ('gallon', 'cup'): 16.0,
            ('cup', 'liter'): 0.236588,
            ('cup', 'milliliter'): 236.588,
            ('cup', 'gallon'): 0.0625,
        }
        if from_unit == to_unit:
            return volume
        key = (from_unit, to_unit)
        if key not in factors:
            raise ValueError(f"Unsupported conversion: {from_unit} to {to_unit}")
        return volume * factors[key]

def convert_volume(volume: float, from_unit: str, to_unit: str) -> float:
    converter = VolumeConverter()
    return converter.convert(volume, from_unit, to_unit)

class TestVolumeConversion(unittest.TestCase):
    def test_zero_volume(self):
        result = convert_volume(0, 'liter', 'gallon')
        self.assertEqual(result, 0.0)

    def test_large_volume(self):
        result = convert_volume(1e12, 'milliliter', 'gallon')
        expected = 1e12 * 0.000264172
        self.assertAlmostEqual(result, expected, places=5)

    def test_same_unit(self):
        result = convert_volume(5.5, 'cup', 'cup')
        self.assertEqual(result, 5.5)

    def test_liter_to_gallon(self):
        result = convert_volume(1.0, 'liter', 'gallon')
        self.assertAlmostEqual(result, 0.264172, places=6)

    def test_gallon_to_liter(self):
        result = convert_volume(1.0, 'gallon', 'liter')
        self.assertAlmostEqual(result, 3.78541, places=5)

    def test_invalid_conversion(self):
        with self.assertRaises(ValueError):
            convert_volume(1.0, 'liter', 'foot')

if __name__ == '__main__':
    conv = VolumeConverter()
    res1 = conv.convert(1.0, 'liter', 'gallon')
    print(res1)
    res2 = convert_volume(100, 'gallon', 'liter')
    print(res2)
    unittest.main()