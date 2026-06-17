import unittest
class TemperatureConverter:
    def to_celsius(self, value):
        return (value - 32) * 5 / 9
    def to_fahrenheit(self, value):
        return (value * 9 / 5) + 32
    def to_kelvin(self, value):
        return value + 273.15
    def to_celsius_from_kelvin(self, value):
        return value - 273.15
    def to_fahrenheit_from_kelvin(self, value):
        return (value - 273.15) * 9 / 5 + 32
class TestTemperatureConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit_exact_match(self):
        converter = TemperatureConverter()
        self.assertAlmostEqual(converter.to_fahrenheit(0), 32, places=6)
    def test_kelvin_conversion_edge_case_zero(self):
        converter = TemperatureConverter()
        result = converter.to_kelvin(-459.67)
        self.assertEqual(result, 0.01)
    def test_celsius_to_fahrenheit_negative_input(self):
        converter = TemperatureConverter()
        self.assertAlmostEqual(converter.to_fahrenheit(-273), -459.67, places=2)
    def test_kelvin_conversion_positive_large_value(self):
        converter = TemperatureConverter()
        result = converter.to_celsius_from_kelvin(1000)
        self.assertEqual(result, 726.85)
if __name__ == '__main__':
    unittest.main(exit=False)