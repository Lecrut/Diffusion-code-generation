import unittest

def convert_volume(volume, from_unit, to_unit):
    conversion_factors = {
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

    factor = conversion_factors.get((from_unit, to_unit))
    if factor is None:
        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")

    return volume * factor

class TestVolumeConversion(unittest.TestCase):
    def test_liter_to_milliliter(self):
        self.assertAlmostEqual(convert_volume(1, 'liter', 'milliliter'), 1000.0)

    def test_liter_to_gallon(self):
        self.assertAlmostEqual(convert_volume(1, 'liter', 'gallon'), 0.264172)

    def test_liter_to_cup(self):
        self.assertAlmostEqual(convert_volume(1, 'liter', 'cup'), 4.22675)

    def test_milliliter_to_liter(self):
        self.assertAlmostEqual(convert_volume(1000, 'milliliter', 'liter'), 1.0)

    def test_milliliter_to_gallon(self):
        self.assertAlmostEqual(convert_volume(1000, 'milliliter', 'gallon'), 0.264172)

    def test_milliliter_to_cup(self):
        self.assertAlmostEqual(convert_volume(1000, 'milliliter', 'cup'), 4.22675)

    def test_gallon_to_liter(self):
        self.assertAlmostEqual(convert_volume(1, 'gallon', 'liter'), 3.78541)

    def test_gallon_to_milliliter(self):
        self.assertAlmostEqual(convert_volume(1, 'gallon', 'milliliter'), 3785.41)

    def test_gallon_to_cup(self):
        self.assertAlmostEqual(convert_volume(1, 'gallon', 'cup'), 16.0)

    def test_cup_to_liter(self):
        self.assertAlmostEqual(convert_volume(1, 'cup', 'liter'), 0.236588)

    def test_cup_to_milliliter(self):
        self.assertAlmostEqual(convert_volume(1, 'cup', 'milliliter'), 236.588)

    def test_cup_to_gallon(self):
        self.assertAlmostEqual(convert_volume(1, 'cup', 'gallon'), 0.0625)

    def test_same_unit(self):
        self.assertAlmostEqual(convert_volume(5.5, 'liter', 'liter'), 5.5)

    def test_zero_volume(self):
        self.assertAlmostEqual(convert_volume(0, 'liter', 'gallon'), 0.0)

    def test_negative_volume(self):
        self.assertAlmostEqual(convert_volume(-1, 'liter', 'gallon'), -0.264172)

    def test_large_volume(self):
        self.assertAlmostEqual(convert_volume(1000000, 'liter', 'gallon'), 264172.0)

    def test_small_volume(self):
        self.assertAlmostEqual(convert_volume(0.001, 'gallon', 'liter'), 0.00378541)

    def test_unsupported_conversion(self):
        with self.assertRaises(ValueError):
            convert_volume(1, 'liter', 'pint')

    def test_float_precision(self):
        result = convert_volume(1.0, 'liter', 'gallon')
        self.assertIsInstance(result, float)

if __name__ == '__main__':
    print(convert_volume(1, 'liter', 'gallon'))
    print(convert_volume(0, 'liter', 'milliliter'))
    print(convert_volume(1000000, 'liter', 'cup'))
    print(convert_volume(5.5, 'gallon', 'liter'))
    unittest.main(argv=[''], exit=False)