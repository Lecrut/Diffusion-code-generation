import unittest
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
class TestTemperatureConversion(unittest.TestCase):
    def test_freezing_point(self):
        self.assertAlmostEqual(convert_celsius_to_fahrenheit(0), 32.0)
    def test_boiling_point(self):
        self.assertAlmostEqual(convert_celsius_to_fahrenheit(100), 212.0)
    def test_negative_temperature(self):
        self.assertAlmostEqual(convert_celsius_to_fahrenheit(-40), -40.0)
    def test_negative_conversion(self):
        self.assertAlmostEqual(convert_celsius_to_fahrenheit(-20), -4.0)
    def test_room_temperature(self):
        self.assertAlmostEqual(convert_celsius_to_fahrenheit(25), 77.0)
    def test_zero_conversion(self):
        self.assertAlmostEqual(convert_celsius_to_fahrenheit(0), 32.0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)