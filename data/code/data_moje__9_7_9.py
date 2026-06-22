import unittest

def convert_volume(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversion_factors = {
        "liter": 1,
        "milliliter": 0.001,
        "gallon": 3.78541,
        "quart": 0.946353,
        "pint": 0.473176,
        "cup": 0.236588,
        "fluid_ounce": 0.0295735
    }
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Unsupported unit")
    liters = value * conversion_factors[from_unit]
    return liters / conversion_factors[to_unit]

class TestVolumeConversion(unittest.TestCase):
    def test_liter_to_gallon(self):
        self.assertAlmostEqual(convert_volume(1, "liter", "gallon"), 0.264172, places=6)
    def test_gallon_to_liter(self):
        self.assertAlmostEqual(convert_volume(1, "gallon", "liter"), 3.78541, places=5)
    def test_same_unit(self):
        self.assertEqual(convert_volume(100, "liter", "liter"), 100)
    def test_zero_volume(self):
        self.assertEqual(convert_volume(0, "gallon", "liter"), 0)
    def test_large_numbers(self):
        self.assertAlmostEqual(convert_volume(1000000, "liter", "milliliter"), 1000000000)
    def test_invalid_unit(self):
        with self.assertRaises(ValueError):
            convert_volume(10, "liter", "invalid_unit")
    def test_milliliter_to_fluid_ounce(self):
        self.assertAlmostEqual(convert_volume(30, "milliliter", "fluid_ounce"), 1.01442, places=5)

if __name__ == '__main__':
    result_liters = convert_volume(50, "liter", "gallon")
    result_gallons = convert_volume(10, "gallon", "liter")
    result_zero = convert_volume(0, "pint", "milliliter")
    result_large = convert_volume(5000000, "milliliter", "liter")
    print(result_liters)
    print(result_gallons)
    print(result_zero)
    print(result_large)
    unittest.main()