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
        self.assertEqual(self.converter.convert_mass(1e6, 2.5), 2500000.0)
    def test_fractional_inputs(self):
        self.assertEqual(self.converter.convert_mass(3.5, 4), 14.0)
        self.assertEqual(self.converter.convert_mass(1.25, 8), 10.0)
    def test_conversion_factor_one(self):
        self.assertEqual(self.converter.convert_mass(7, 1), 7)
        self.assertEqual(self.converter.convert_mass(99, 1), 99)
    def test_negative_mass(self):
        self.assertEqual(self.converter.convert_mass(-5, 2), -10)
        self.assertEqual(self.converter.convert_mass(-100, 0.1), -10.0)
    def test_zero_conversion_factor(self):
        self.assertEqual(self.converter.convert_mass(50, 0), 0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)