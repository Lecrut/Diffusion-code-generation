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
        self.assertEqual(self.converter.convert_mass(0, 0.001), 0.0)
    def test_large_numbers(self):
        self.assertEqual(self.converter.convert_mass(10000, 1.5), 15000.0)
        self.assertEqual(self.converter.convert_mass(1e6, 0.01), 10000.0)
    def test_fractional_results(self):
        self.assertEqual(self.converter.convert_mass(3, 3.333), 9.999)
        self.assertAlmostEqual(self.converter.convert_mass(1, 7), 7.0)
    def test_negative_mass(self):
        self.assertEqual(self.converter.convert_mass(-10, 2), -20)
        self.assertEqual(self.converter.convert_mass(-5, 0.5), -2.5)
    def test_conversion_factor_one(self):
        self.assertEqual(self.converter.convert_mass(42, 1), 42)
    def test_zero_conversion_factor(self):
        self.assertEqual(self.converter.convert_mass(50, 0), 0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)