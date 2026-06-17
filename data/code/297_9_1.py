import unittest
def convert_temperature(celsius):
    kelvin = celsius + 273.15
    fahrenheit = (celsius * 9/5) + 32
    return {"kelvin": kelvin, "fahrenheit": fahrenheit}
def convert_mass(kg):
    pound = kg * 2.20462
    return pound
class TestConversionFunctions(unittest.TestCase):
    def test_temperature_freezing(self):
        celsius = 0
        result = convert_temperature(celsius)
        self.assertAlmostEqual(result["kelvin"], 273.15)
        self.assertAlmostEqual(result["fahrenheit"], 32.0)
    def test_temperature_boiling(self):
        celsius = 100
        result = convert_temperature(celsius)
        self.assertAlmostEqual(result["kelvin"], 373.15)
        self.assertAlmostEqual(result["fahrenheit"], 212.0)
    def test_temperature_negative(self):
        celsius = -40
        result = convert_temperature(celsius)
        self.assertAlmostEqual(result["kelvin"], -13.15)
        self.assertAlmostEqual(result["fahrenheit"], -40.0)
    def test_temperature_zero_edge_case(self):
        celsius = 0.0
        result = convert_temperature(celsius)
        self.assertAlmostEqual(result["kelvin"], 273.15)
        self.assertAlmostEqual(result["fahrenheit"], 32.0)
    def test_temperature_extreme_high(self):
        celsius = 500
        result = convert_temperature(celsius)
        self.assertAlmostEqual(result["kelvin"], 773.15)
        self.assertAlmostEqual(result["fahrenheit"], 932.0)
    def test_mass_zero_edge_case(self):
        kg = 0
        result = convert_mass(kg)
        self.assertEqual(result, 0.0)
    def test_mass_standard_value(self):
        kg = 1
        result = convert_mass(kg)
        self.assertAlmostEqual(result, 2.20462)
    def test_mass_large_value(self):
        kg = 1000
        result = convert_mass(kg)
        self.assertAlmostEqual(result, 2204.62)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)