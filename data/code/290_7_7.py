import unittest
class MassConverter:
    def convert_mass(self, mass_kg, conversion_factor):
        return mass_kg * conversion_factor
class TestMassConverter(unittest.TestCase):
    def setUp(self):
        self.converter = MassConverter()
    def test_basic_conversion(self):
        self.assertEqual(self.converter.convert_mass(10, 2), 20)
        self.assertEqual(self.converter.convert_mass(5, 0.5), 2.5)
    def test_zero_mass(self):
        self.assertEqual(self.converter.convert_mass(0, 10), 0)
        self.assertEqual(self.converter.convert_mass(0, -5), 0)
    def test_large_numbers(self):
        self.assertEqual(self.converter.convert_mass(10000, 0.01), 100)
        self.assertEqual(self.converter.convert_mass(1e6, 3.14), 3141592.653589793)
    def test_negative_mass(self):
        self.assertEqual(self.converter.convert_mass(-10, 2), -20)
        self.assertEqual(self.converter.convert_mass(-5, -1), 5)
    def test_conversion_factor_one(self):
        self.assertEqual(self.converter.convert_mass(42, 1), 42)
    def test_conversion_factor_zero(self):
        self.assertEqual(self.converter.convert_mass(999, 0), 0)
    def test_float_precision(self):
        result = self.converter.convert_mass(1, 3.14159)
        expected = 3.14159
        self.assertAlmostEqual(result, expected)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)