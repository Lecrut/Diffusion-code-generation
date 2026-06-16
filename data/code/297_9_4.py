import unittest
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
class TestConversionFunctions(unittest.TestCase):
    def test_celsius_to_fahrenheit_freezing_point(self):
        self.assertAlmostEqual(convert_celsius_to_fahrenheit(0), 32.0)
    def test_celsius_to_fahrenheit_boiling_point(self):
        self.assertAlmostEqual(convert_celsius_to_fahrenheit(100), 212.0)
    def test_celsius_to_fahrenheit_negative_value(self):
        self.assertAlmostEqual(convert_celsius_to_fahrenheit(-40), -40.0)
    def test_celsius_to_fahrenheit_zero_value(self):
        self.assertAlmostEqual(convert_celsius_to_fahrenheit(0), 32.0)
    def test_celsius_to_fahrenheit_extreme_high(self):
        self.assertAlmostEqual(convert_celsius_to_fahrenheit(500), 932.0)
    def test_celsius_to_fahrenheit_extreme_low(self):
        self.assertAlmostEqual(convert_celsius_to_fahrenheit(-100), -148.0)
    def test_fahrenheit_to_celsius_freezing_point(self):
        self.assertAlmostEqual(convert_fahrenheit_to_celsius(32), 0.0)
    def test_fahrenheit_to_celsius_boiling_point(self):
        self.assertAlmostEqual(convert_fahrenheit_to_celsius(212), 100.0)
    def test_fahrenheit_to_celsius_zero_value(self):
        self.assertAlmostEqual(convert_fahrenheit_to_celsius(0), -17.77777777777778)
    def test_fahrenheit_to_celsius_negative_value(self):
        self.assertAlmostEqual(convert_fahrenheit_to_celsius(-40), -40.0)
    def test_fahrenheit_to_celsius_extreme_high(self):
        self.assertAlmostEqual(convert_fahrenheit_to_celsius(1000), 555.5555555555555)
    def test_fahrenheit_to_celsius_extreme_low(self):
        self.assertAlmostEqual(convert_fahrenheit_to_celsius(-60), -51.11111111111111)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)