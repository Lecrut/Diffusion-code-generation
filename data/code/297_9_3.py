import unittest
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
class TestConversionFunctions(unittest.TestCase):
    def test_celsius_to_fahrenheit_freezing(self):
        self.assertAlmostEqual(convert_celsius_to_fahrenheit(0), 32.0)
    def test_celsius_to_fahrenheit_boiling(self):
        self.assertAlmostEqual(convert_celsius_to_fahrenheit(100), 212.0)
    def test_celsius_to_fahrenheit_negative(self):
        self.assertAlmostEqual(convert_celsius_to_fahrenheit(-40), -40.0)
    def test_celsius_to_fahrenheit_zero(self):
        self.assertAlmostEqual(convert_celsius_to_fahrenheit(0), 32.0)
    def test_celsius_to_fahrenheit_extreme_positive(self):
        self.assertAlmostEqual(convert_celsius_to_fahrenheit(500), 932.0)
    def test_celsius_to_fahrenheit_extreme_negative(self):
        self.assertAlmostEqual(convert_celsius_to_fahrenheit(-100), -148.0)
    def test_fahrenheit_to_celsius_freezing(self):
        self.assertAlmostEqual(convert_fahrenheit_to_celsius(32), 0.0)
    def test_fahrenheit_to_celsius_boiling(self):
        self.assertAlmostEqual(convert_fahrenheit_to_celsius(212), 100.0)
    def test_fahrenheit_to_celsius_zero(self):
        self.assertAlmostEqual(convert_fahrenheit_to_celsius(50), 10.0)
    def test_fahrenheit_to_celsius_negative(self):
        self.assertAlmostEqual(convert_fahrenheit_to_celsius(-40), -40.0)
    def test_conversion_roundtrip(self):
        test_values = [0, 100, -40, 212, -40]
        for c in test_values:
            f = convert_celsius_to_fahrenheit(c)
            c_back = convert_fahrenheit_to_celsius(f)
            self.assertAlmostEqual(c_back, c, places=7)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)