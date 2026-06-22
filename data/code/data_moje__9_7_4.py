import unittest

CONVERSION_RATES = {
    'liter': 1.0,
    'milliliter': 0.001,
    'gallon': 3.785411784,
    'quart': 0.946352946,
    'pint': 0.473176473,
    'cup': 0.2365882365,
    'tablespoon': 0.01478676478125,
    'teaspoon': 0.00492892159375,
    'cubic_meter': 1000.0,
    'cubic_centimeter': 0.001,
    'fluid_ounce': 0.0295735295625,
}

class VolumeConverter:
    def __init__(self):
        self._rates = CONVERSION_RATES

    def convert(self, value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Volume value must be a number")
        if value < 0:
            raise ValueError("Volume value cannot be negative")
        
        from_key = from_unit.lower()
        to_key = to_unit.lower()

        if from_key not in self._rates:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_key not in self._rates:
            raise ValueError(f"Unsupported target unit: {to_unit}")

        if value == 0:
            return 0.0

        liters = value * self._rates[from_key]
        result = liters / self._rates[to_key]
        return result

class TestVolumeConverter(unittest.TestCase):
    def setUp(self):
        self.converter = VolumeConverter()

    def test_liter_to_liter(self):
        self.assertAlmostEqual(self.converter.convert(10, 'liter', 'liter'), 10.0)

    def test_gallon_to_liter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'gallon', 'liter'), 3.785411784)

    def test_liter_to_gallon(self):
        self.assertAlmostEqual(self.converter.convert(1, 'liter', 'gallon'), 0.2641720523581484)

    def test_milliliter_to_liter(self):
        self.assertAlmostEqual(self.converter.convert(1000, 'milliliter', 'liter'), 1.0)

    def test_liter_to_milliliter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'liter', 'milliliter'), 1000.0)

    def test_zero_volume(self):
        self.assertEqual(self.converter.convert(0, 'gallon', 'liter'), 0.0)
        self.assertEqual(self.converter.convert(0, 'liter', 'cup'), 0.0)

    def test_large_number_conversion(self):
        large_val = 1000000000.0
        result = self.converter.convert(large_val, 'liter', 'gallon')
        expected = large_val * 0.2641720523581484
        self.assertAlmostEqual(result, expected)

    def test_negative_volume_raises(self):
        with self.assertRaises(ValueError):
            self.converter.convert(-5, 'liter', 'gallon')

    def test_invalid_source_unit_raises(self):
        with self.assertRaises(ValueError):
            self.converter.convert(10, 'invalid_unit', 'liter')

    def test_invalid_target_unit_raises(self):
        with self.assertRaises(ValueError):
            self.converter.convert(10, 'liter', 'invalid_unit')

    def test_fluid_ounce_to_milliliter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'fluid_ounce', 'milliliter'), 29.5735295625)

    def test_cubic_meter_to_liter(self):
        self.assertEqual(self.converter.convert(1, 'cubic_meter', 'liter'), 1000.0)

    def test_tablespoon_to_teaspoon(self):
        self.assertAlmostEqual(self.converter.convert(1, 'tablespoon', 'teaspoon'), 3.0)

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_result = converter.convert(100, 'gallon', 'liter')
    print(f"100 gallons equals {sample_result} liters")
    
    zero_result = converter.convert(0, 'cup', 'tablespoon')
    print(f"0 cups equals {zero_result} tablespoons")
    
    large_result = converter.convert(5000000, 'milliliter', 'cubic_meter')
    print(f"5,000,000 milliliters equals {large_result} cubic meters")