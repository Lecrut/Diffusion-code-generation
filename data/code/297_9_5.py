import unittest
def convert_temperature(celsius):
    return (celsius * 9/5) + 32
def convert_mass(kg):
    return kg * 2.20462
class TestConversionFunctions(unittest.TestCase):
    def test_convert_temperature_freezing(self):
        self.assertAlmostEqual(convert_temperature(0), 32.0)
    def test_convert_temperature_boiling(self):
        self.assertAlmostEqual(convert_temperature(100), 212.0)
    def test_convert_temperature_negative(self):
        self.assertAlmostEqual(convert_temperature(-40), -40.0)
    def test_convert_temperature_positive(self):
        self.assertAlmostEqual(convert_temperature(20), 68.0)
    def test_convert_temperature_zero(self):
        self.assertAlmostEqual(convert_temperature(0), 32.0)
    def test_convert_temperature_extreme_high(self):
        self.assertAlmostEqual(convert_temperature(500), 932.0)
    def test_convert_temperature_extreme_low(self):
        self.assertAlmostEqual(convert_temperature(-100), -17.2)
    def test_convert_mass_zero(self):
        self.assertEqual(convert_mass(0), 0.0)
    def test_convert_mass_standard(self):
        self.assertAlmostEqual(convert_mass(1), 2.20462)
    def test_convert_mass_large_value(self):
        self.assertAlmostEqual(convert_mass(1000), 2204.62)
    def test_convert_mass_small_value(self):
        self.assertAlmostEqual(convert_mass(0.5), 1.10231)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)