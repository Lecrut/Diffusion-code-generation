import unittest

def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    liters_map = {
        "liter": 1.0,
        "litre": 1.0,
        "gallon": 3.78541,
        "quart": 0.946353,
        "pint": 0.473176,
        "cup": 0.236588,
        "tablespoon": 0.0147868,
        "teaspoon": 0.00492892,
        "milliliter": 0.001,
        "millilitre": 0.001,
        "cubic_meter": 1000.0,
        "cubic_centimeter": 0.001,
    }

    if from_unit not in liters_map:
        raise ValueError(f"Unknown source unit: {from_unit}")
    if to_unit not in liters_map:
        raise ValueError(f"Unknown target unit: {to_unit}")

    value_in_liters = value * liters_map[from_unit]
    result = value_in_liters / liters_map[to_unit]
    return result

class TestVolumeConversion(unittest.TestCase):

    def test_zero_volume(self):
        result = convert_volume(0, "liter", "gallon")
        self.assertAlmostEqual(result, 0.0)

    def test_negative_volume(self):
        result = convert_volume(-10, "liter", "liter")
        self.assertAlmostEqual(result, -10.0)

    def test_identity_conversion(self):
        result = convert_volume(100, "liter", "liter")
        self.assertAlmostEqual(result, 100.0)

    def test_liter_to_gallon(self):
        result = convert_volume(1, "liter", "gallon")
        self.assertAlmostEqual(result, 1.0 / 3.78541, places=5)

    def test_gallon_to_liter(self):
        result = convert_volume(1, "gallon", "liter")
        self.assertAlmostEqual(result, 3.78541, places=5)

    def test_large_numbers(self):
        result = convert_volume(1e9, "milliliter", "cubic_meter")
        self.assertAlmostEqual(result, 1e9 * 0.001 / 1000.0)

    def test_uk_vs_us_units(self):
        result = convert_volume(1, "liter", "milliliter")
        self.assertAlmostEqual(result, 1000.0)

    def test_invalid_source_unit(self):
        with self.assertRaises(ValueError):
            convert_volume(1, "invalid_unit", "liter")

    def test_invalid_target_unit(self):
        with self.assertRaises(ValueError):
            convert_volume(1, "liter", "invalid_unit")

    def test_cup_to_teaspoon(self):
        result = convert_volume(1, "cup", "teaspoon")
        self.assertAlmostEqual(result, 0.236588 / 0.00492892, places=5)

if __name__ == '__main__':
    print(convert_volume(5, "gallon", "liter"))
    print(convert_volume(1000, "milliliter", "liter"))
    print(convert_volume(0, "liter", "gallon"))
    unittest.main()