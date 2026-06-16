import unittest
def convert_mass(mass_kg, conversion_factor):
    return mass_kg * conversion_factor
class TestMassConversion(unittest.TestCase):
    def test_positive_conversion(self):
        self.assertEqual(convert_mass(10.0, 2.20462), 22.0462)
    def test_zero_mass(self):
        self.assertEqual(convert_mass(0.0, 2.20462), 0.0)
    def test_large_values(self):
        self.assertEqual(convert_mass(1000.0, 2.20462), 2204.62)
    def test_small_values(self):
        self.assertAlmostEqual(convert_mass(0.001, 2.20462), 0.00220462)
    def test_integer_input(self):
        self.assertEqual(convert_mass(5, 2.20462), 11.0231)
    def test_float_input_precision(self):
        factor = 3.14159
        self.assertAlmostEqual(convert_mass(1.0, factor), 3.14159)
    def test_negative_mass(self):
        self.assertEqual(convert_mass(-5.0, 2.20462), -11.0231)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)