import unittest
class MassConverter:
    def convert_mass(self, mass_kg, conversion_factor):
        return mass_kg * conversion_factor
class TestMassConverter(unittest.TestCase):
    def setUp(self):
        self.converter = MassConverter()
    def test_positive_conversion(self):
        mass_kg = 10.0
        conversion_factor = 2.5
        expected = 25.0
        self.assertEqual(self.converter.convert_mass(mass_kg, conversion_factor), expected)
    def test_zero_mass(self):
        mass_kg = 0.0
        conversion_factor = 10.0
        expected = 0.0
        self.assertEqual(self.converter.convert_mass(mass_kg, conversion_factor), expected)
    def test_large_numbers(self):
        mass_kg = 1000.0
        conversion_factor = 0.5
        expected = 500.0
        self.assertEqual(self.converter.convert_mass(mass_kg, conversion_factor), expected)
    def test_fractional_result(self):
        mass_kg = 3.0
        conversion_factor = 1.5
        expected = 4.5
        self.assertEqual(self.converter.convert_mass(mass_kg, conversion_factor), expected)
    def test_conversion_to_zero(self):
        mass_kg = 5.0
        conversion_factor = 0.0
        expected = 0.0
        self.assertEqual(self.converter.convert_mass(mass_kg, conversion_factor), expected)
    def test_negative_mass(self):
        mass_kg = -10.0
        conversion_factor = 2.0
        expected = -20.0
        self.assertEqual(self.converter.convert_mass(mass_kg, conversion_factor), expected)
    def test_negative_conversion_factor(self):
        mass_kg = 10.0
        conversion_factor = -2.0
        expected = -20.0
        self.assertEqual(self.converter.convert_mass(mass_kg, conversion_factor), expected)
    def test_floating_point_precision(self):
        mass_kg = 1.0
        conversion_factor = 3.33
        expected = 3.33
        self.assertAlmostEqual(self.converter.convert_mass(mass_kg, conversion_factor), expected)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)