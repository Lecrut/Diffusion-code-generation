import unittest

def convert_volume(value, from_unit, to_unit):
    conversions = {
        'ml_to_l': 0.001,
        'l_to_ml': 1000,
        'ml_to_gal': 0.000264172,
        'gal_to_ml': 3785.41,
        'l_to_gal': 0.264172,
        'gal_to_l': 3.78541,
        'oz_to_ml': 29.5735,
        'ml_to_oz': 0.033814,
        'oz_to_l': 0.0295735,
        'l_to_oz': 33.814,
        'cup_to_ml': 236.588,
        'ml_to_cup': 0.00422675,
        'cup_to_l': 0.236588,
        'l_to_cup': 4.22675,
        'pint_to_ml': 473.176,
        'ml_to_pint': 0.00211338,
        'pint_to_l': 0.473176,
        'l_to_pint': 2.11338,
        'quart_to_ml': 946.353,
        'ml_to_quart': 0.00105669,
        'quart_to_l': 0.946353,
        'l_to_quart': 1.05669,
    }
    key = f"{from_unit}_to_{to_unit}"
    if from_unit == to_unit:
        return value
    if key not in conversions:
        raise ValueError(f"Unsupported conversion: {from_unit} to {to_unit}")
    if value < 0:
        raise ValueError("Volume cannot be negative")
    return value * conversions[key]

class TestVolumeConversion(unittest.TestCase):
    def test_identity_conversion(self):
        self.assertEqual(convert_volume(5, 'l', 'l'), 5)
        self.assertEqual(convert_volume(100, 'ml', 'ml'), 100)

    def test_zero_volume(self):
        self.assertEqual(convert_volume(0, 'l', 'ml'), 0)
        self.assertEqual(convert_volume(0, 'gal', 'l'), 0)
        self.assertEqual(convert_volume(0, 'ml', 'oz'), 0)

    def test_negative_volume_raises(self):
        with self.assertRaises(ValueError):
            convert_volume(-1, 'l', 'ml')
        with self.assertRaises(ValueError):
            convert_volume(-100, 'gal', 'l')

    def test_unsupported_units_raises(self):
        with self.assertRaises(ValueError):
            convert_volume(5, 'cubic_feet', 'ml')
        with self.assertRaises(ValueError):
            convert_volume(5, 'l', 'barrels')

    def test_ml_to_l(self):
        self.assertAlmostEqual(convert_volume(1000, 'ml', 'l'), 1.0)
        self.assertAlmostEqual(convert_volume(500, 'ml', 'l'), 0.5)

    def test_l_to_ml(self):
        self.assertAlmostEqual(convert_volume(1, 'l', 'ml'), 1000.0)
        self.assertAlmostEqual(convert_volume(0.5, 'l', 'ml'), 500.0)

    def test_l_to_gal(self):
        self.assertAlmostEqual(convert_volume(1, 'l', 'gal'), 0.264172, places=5)
        self.assertAlmostEqual(convert_volume(3.78541, 'l', 'gal'), 1.0, places=5)

    def test_gal_to_l(self):
        self.assertAlmostEqual(convert_volume(1, 'gal', 'l'), 3.78541, places=5)
        self.assertAlmostEqual(convert_volume(0.264172, 'gal', 'l'), 1.0, places=5)

    def test_ml_to_gal(self):
        self.assertAlmostEqual(convert_volume(3785.41, 'ml', 'gal'), 1.0, places=5)
        self.assertAlmostEqual(convert_volume(1, 'ml', 'gal'), 0.000264172, places=7)

    def test_gal_to_ml(self):
        self.assertAlmostEqual(convert_volume(1, 'gal', 'ml'), 3785.41, places=5)
        self.assertAlmostEqual(convert_volume(0.000264172, 'gal', 'ml'), 1.0, places=5)

    def test_oz_to_ml(self):
        self.assertAlmostEqual(convert_volume(1, 'oz', 'ml'), 29.5735, places=4)
        self.assertAlmostEqual(convert_volume(33.814, 'oz', 'ml'), 1000.0, places=5)

    def test_ml_to_oz(self):
        self.assertAlmostEqual(convert_volume(29.5735, 'ml', 'oz'), 1.0, places=5)
        self.assertAlmostEqual(convert_volume(1000, 'ml', 'oz'), 33.814, places=5)

    def test_cup_to_ml(self):
        self.assertAlmostEqual(convert_volume(1, 'cup', 'ml'), 236.588, places=5)
        self.assertAlmostEqual(convert_volume(4.22675, 'cup', 'ml'), 1000.0, places=5)

    def test_ml_to_cup(self):
        self.assertAlmostEqual(convert_volume(236.588, 'ml', 'cup'), 1.0, places=5)
        self.assertAlmostEqual(convert_volume(1000, 'ml', 'cup'), 4.22675, places=5)

    def test_pint_to_ml(self):
        self.assertAlmostEqual(convert_volume(1, 'pint', 'ml'), 473.176, places=5)
        self.assertAlmostEqual(convert_volume(2.11338, 'pint', 'ml'), 1000.0, places=5)

    def test_ml_to_pint(self):
        self.assertAlmostEqual(convert_volume(473.176, 'ml', 'pint'), 1.0, places=5)
        self.assertAlmostEqual(convert_volume(1000, 'ml', 'pint'), 2.11338, places=5)

    def test_quart_to_ml(self):
        self.assertAlmostEqual(convert_volume(1, 'quart', 'ml'), 946.353, places=5)
        self.assertAlmostEqual(convert_volume(1.05669, 'quart', 'ml'), 1000.0, places=5)

    def test_ml_to_quart(self):
        self.assertAlmostEqual(convert_volume(946.353, 'ml', 'quart'), 1.0, places=5)
        self.assertAlmostEqual(convert_volume(1000, 'ml', 'quart'), 1.05669, places=5)

    def test_large_numbers(self):
        self.assertAlmostEqual(convert_volume(1e12, 'ml', 'l'), 1e9, places=2)
        self.assertAlmostEqual(convert_volume(1e12, 'l', 'gal'), 2.64172e11, places=5)
        self.assertAlmostEqual(convert_volume(1e12, 'gal', 'ml'), 3.78541e15, places=5)

    def test_float_precision(self):
        result = convert_volume(0.001, 'l', 'ml')
        self.assertAlmostEqual(result, 1.0, places=5)

    def test_round_trip_l_ml(self):
        original = 123.456
        converted = convert_volume(original, 'l', 'ml')
        back = convert_volume(converted, 'ml', 'l')
        self.assertAlmostEqual(original, back, places=4)

    def test_round_trip_gal_l(self):
        original = 10.5
        converted = convert_volume(original, 'gal', 'l')
        back = convert_volume(converted, 'l', 'gal')
        self.assertAlmostEqual(original, back, places=4)

    def test_small_positive_values(self):
        self.assertAlmostEqual(convert_volume(1e-6, 'ml', 'l'), 1e-9, places=12)
        self.assertAlmostEqual(convert_volume(1e-9, 'l', 'ml'), 1e-6, places=12)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)