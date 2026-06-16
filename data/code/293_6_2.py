import unittest
def convert_mass(mass_kg):
    mass_lbs = mass_kg * 2.20462
    return mass_lbs
def convert_length(length_m):
    length_ft = length_m * 3.28084
    return length_ft
class TestConversions(unittest.TestCase):
    def test_mass_conversion(self):
        self.assertAlmostEqual(convert_mass(0), 0.0)
        self.assertAlmostEqual(convert_mass(1), 2.20462)
        self.assertAlmostEqual(convert_mass(10), 22.0462)
        self.assertAlmostEqual(convert_mass(50), 110.231)
    def test_length_conversion(self):
        self.assertAlmostEqual(convert_length(0), 0.0)
        self.assertAlmostEqual(convert_length(1), 3.28084)
        self.assertAlmostEqual(convert_length(10), 32.8084)
        self.assertAlmostEqual(convert_length(5), 16.4042)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)