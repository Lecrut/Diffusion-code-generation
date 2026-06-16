import unittest
def convert_mass(mass_kg):
    mass_lbs = mass_kg * 2.20462
    return mass_lbs
def convert_length(length_m):
    length_mi = length_m / 1609.344
    return length_mi
class TestConversions(unittest.TestCase):
    def test_mass_conversion(self):
        self.assertAlmostEqual(convert_mass(0), 0.0)
        self.assertAlmostEqual(convert_mass(1), 2.20462)
        self.assertAlmostEqual(convert_mass(10), 22.0462)
        self.assertAlmostEqual(convert_mass(100), 220.462)
    def test_length_conversion(self):
        self.assertAlmostEqual(convert_length(0), 0.0)
        self.assertAlmostEqual(convert_length(1609.344), 1.0)
        self.assertAlmostEqual(convert_length(3218.688), 2.0)
        self.assertAlmostEqual(convert_length(1000), 0.621371)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)