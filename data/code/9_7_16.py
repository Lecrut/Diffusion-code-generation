import unittest

class VolumeConverter:

    def __init__(self):
        self.to_liters = {'liter': 1.0, 'milliliter': 0.001, 'gallon_us': 3.78541, 'gallon_imp': 4.54609, 'quart_us': 0.946353, 'pint_us': 0.473176, 'cup_us': 0.236588, 'fluid_ounce_us': 0.0295735, 'tablespoon_us': 0.0147868, 'teaspoon_us': 0.00492892, 'cubic_meter': 1000.0, 'cubic_centimeter': 0.001, 'cubic_inch': 0.0163871, 'cubic_foot': 28.3168, 'barrel_oil': 158.987, 'barrel_us_dry': 115.627}

    def convert(self, value, from_unit, to_unit):
        if value < 0:
            raise ValueError('Volume cannot be negative')
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        if from_unit not in self.to_liters:
            raise ValueError(f'Invalid source unit: {from_unit}')
        if to_unit not in self.to_liters:
            raise ValueError(f'Invalid target unit: {to_unit}')
        liters = value * self.to_liters[from_unit]
        return liters / self.to_liters[to_unit]

class TestVolumeConverter(unittest.TestCase):

    def setUp(self):
        self.converter = VolumeConverter()

    def test_basic_conversion_liter_to_milliliter(self):
        result = self.converter.convert(1.0, 'liter', 'milliliter')
        self.assertAlmostEqual(result, 1000.0, places=5)

    def test_basic_conversion_milliliter_to_liter(self):
        result = self.converter.convert(1000.0, 'milliliter', 'liter')
        self.assertAlmostEqual(result, 1.0, places=5)

    def test_gallon_us_to_liters(self):
        result = self.converter.convert(1.0, 'gallon_us', 'liter')
        self.assertAlmostEqual(result, 3.78541, places=4)

    def test_liters_to_gallon_imp(self):
        result = self.converter.convert(4.54609, 'liter', 'gallon_imp')
        self.assertAlmostEqual(result, 1.0, places=4)

    def test_zero_volume(self):
        result = self.converter.convert(0.0, 'liter', 'gallon_us')
        self.assertEqual(result, 0.0)

    def test_zero_volume_different_units(self):
        result = self.converter.convert(0.0, 'milliliter', 'cubic_meter')
        self.assertEqual(result, 0.0)

    def test_large_number_conversion(self):
        large_value = 1000000000000000.0
        result = self.converter.convert(large_value, 'liter', 'milliliter')
        expected = large_value * 1000.0
        self.assertAlmostEqual(result, expected, places=0)

    def test_very_small_number_conversion(self):
        small_value = 1e-10
        result = self.converter.convert(small_value, 'milliliter', 'liter')
        expected = small_value * 0.001
        self.assertAlmostEqual(result, expected, places=15)

    def test_same_unit_conversion(self):
        result = self.converter.convert(5.5, 'liter', 'liter')
        self.assertAlmostEqual(result, 5.5, places=10)

    def test_negative_volume_raises_error(self):
        with self.assertRaises(ValueError):
            self.converter.convert(-1.0, 'liter', 'milliliter')

    def test_negative_volume_zero_boundary(self):
        with self.assertRaises(ValueError):
            self.converter.convert(-0.0001, 'gallon_us', 'liter')

    def test_invalid_from_unit(self):
        with self.assertRaises(ValueError):
            self.converter.convert(1.0, 'invalid_unit', 'liter')

    def test_invalid_to_unit(self):
        with self.assertRaises(ValueError):
            self.converter.convert(1.0, 'liter', 'invalid_unit')

    def test_both_units_invalid(self):
        with self.assertRaises(ValueError):
            self.converter.convert(1.0, 'invalid1', 'invalid2')

    def test_case_insensitive_units(self):
        result1 = self.converter.convert(1.0, 'Liter', 'MILLILITER')
        result2 = self.converter.convert(1.0, 'LITER', 'milliliter')
        self.assertAlmostEqual(result1, result2, places=5)

    def test_cubic_meter_conversion(self):
        result = self.converter.convert(1.0, 'cubic_meter', 'liter')
        self.assertAlmostEqual(result, 1000.0, places=5)

    def test_cubic_inches_to_liters(self):
        result = self.converter.convert(1.0, 'cubic_inch', 'liter')
        self.assertAlmostEqual(result, 0.0163871, places=5)

    def test_barrel_oil_conversion(self):
        result = self.converter.convert(1.0, 'barrel_oil', 'gallon_us')
        expected = 158.987 / 3.78541
        self.assertAlmostEqual(result, expected, places=4)

    def test_floating_point_precision(self):
        result = self.converter.convert(0.333333, 'liter', 'milliliter')
        self.assertAlmostEqual(result, 333.333, places=3)

    def test_maximum_float_value_safe(self):
        max_safe = 1e+300
        result = self.converter.convert(max_safe, 'liter', 'milliliter')
        self.assertEqual(result, float('inf'))

    def test_minimum_positive_float(self):
        min_positive = 1e-300
        result = self.converter.convert(min_positive, 'liter', 'milliliter')
        self.assertAlmostEqual(result, min_positive * 1000, places=300)

    def test_multiple_conversions_chain(self):
        val = 10.0
        r1 = self.converter.convert(val, 'liter', 'gallon_us')
        r2 = self.converter.convert(r1, 'gallon_us', 'milliliter')
        r3 = self.converter.convert(r2, 'milliliter', 'liter')
        self.assertAlmostEqual(r3, val, places=4)

    def test_us_cup_conversion(self):
        result = self.converter.convert(1.0, 'cup_us', 'liter')
        self.assertAlmostEqual(result, 0.236588, places=5)

    def test_teaspoon_conversion(self):
        result = self.converter.convert(1.0, 'teaspoon_us', 'milliliter')
        self.assertAlmostEqual(result, 4.92892, places=4)

    def test_quart_to_pint_relationship(self):
        result = self.converter.convert(1.0, 'quart_us', 'pint_us')
        self.assertAlmostEqual(result, 2.0, places=5)

    def test_fluid_ounce_to_tablespoon(self):
        result = self.converter.convert(2.0, 'fluid_ounce_us', 'tablespoon_us')
        self.assertAlmostEqual(result, 2.0, places=5)

    def test_cubic_foot_to_liters(self):
        result = self.converter.convert(1.0, 'cubic_foot', 'liter')
        self.assertAlmostEqual(result, 28.3168, places=4)

    def test_dry_barrel_conversion(self):
        result = self.converter.convert(1.0, 'barrel_us_dry', 'liter')
        self.assertAlmostEqual(result, 115.627, places=3)

    def test_edge_case_very_large(self):
        large = 1e+50
        result = self.converter.convert(large, 'liter', 'cubic_meter')
        self.assertEqual(result, large * 0.001)

    def test_edge_case_small_positive(self):
        small = 1e-50
        result = self.converter.convert(small, 'liter', 'milliliter')
        self.assertAlmostEqual(result, small * 1000, places=100)

def main():
    converter = VolumeConverter()
    print(converter.convert(1.0, 'liter', 'milliliter'))
    print(converter.convert(0.0, 'liter', 'gallon_us'))
    print(converter.convert(1000000000000000.0, 'liter', 'milliliter'))
    print(converter.convert(1.0, 'gallon_us', 'liter'))
    print(converter.convert(5.5, 'liter', 'liter'))
    print(converter.convert(1.0, 'cubic_meter', 'liter'))
    print(converter.convert(1.0, 'cup_us', 'liter'))
    print(converter.convert(10.0, 'liter', 'gallon_us'))
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestVolumeConverter)
    unittest.TextTestRunner(verbosity=0).run(test_suite)
if __name__ == '__main__':
    main()