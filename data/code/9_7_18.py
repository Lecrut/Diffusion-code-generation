import unittest

class VolumeConverter:
    def __init__(self, volume, unit):
        self.volume = volume
        self.unit = unit

    def to_liters(self):
        conversions = {
            "ml": 0.001,
            "liter": 1.0,
            "gallon": 3.78541,
            "quart": 0.946353,
            "pint": 0.473176,
            "cup": 0.236588,
            "tablespoon": 0.0147868,
            "teaspoon": 0.00492892,
            "cubic_meter": 1000.0,
            "cubic_centimeter": 0.001,
        }
        if self.unit not in conversions:
            raise ValueError(f"Unsupported unit: {self.unit}")
        return self.volume * conversions[self.unit]

    def convert(self, target_unit):
        liters = self.to_liters()
        conversions = {
            "ml": 0.001,
            "liter": 1.0,
            "gallon": 3.78541,
            "quart": 0.946353,
            "pint": 0.473176,
            "cup": 0.236588,
            "tablespoon": 0.0147868,
            "teaspoon": 0.00492892,
            "cubic_meter": 1000.0,
            "cubic_centimeter": 0.001,
        }
        if target_unit not in conversions:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        if conversions[target_unit] == 0:
            raise ValueError("Conversion factor cannot be zero")
        return liters / conversions[target_unit]

def convert_volume(volume, source_unit, target_unit):
    converter = VolumeConverter(volume, source_unit)
    return converter.convert(target_unit)

class TestVolumeConversion(unittest.TestCase):

    def test_zero_volume(self):
        self.assertAlmostEqual(convert_volume(0, "liter", "gallon"), 0.0, places=9)
        self.assertAlmostEqual(convert_volume(0, "gallon", "liter"), 0.0, places=9)
        self.assertAlmostEqual(convert_volume(0, "ml", "cubic_meter"), 0.0, places=9)

    def test_large_volume(self):
        result = convert_volume(1e9, "ml", "liter")
        self.assertAlmostEqual(result, 1e6, places=2)
        result = convert_volume(1e6, "liter", "gallon")
        self.assertAlmostEqual(result, 1e6 / 3.78541, places=4)

    def test_same_unit(self):
        self.assertAlmostEqual(convert_volume(5, "liter", "liter"), 5.0, places=9)
        self.assertAlmostEqual(convert_volume(10.5, "gallon", "gallon"), 10.5, places=9)

    def test_basic_liter_to_gallon(self):
        result = convert_volume(1, "liter", "gallon")
        self.assertAlmostEqual(result, 1 / 3.78541, places=5)

    def test_basic_gallon_to_liter(self):
        result = convert_volume(1, "gallon", "liter")
        self.assertAlmostEqual(result, 3.78541, places=4)

    def test_ml_to_cubic_centimeter(self):
        self.assertAlmostEqual(convert_volume(500, "ml", "cubic_centimeter"), 500.0, places=9)

    def test_cubic_meter_to_liter(self):
        self.assertAlmostEqual(convert_volume(1, "cubic_meter", "liter"), 1000.0, places=9)

    def test_invalid_source_unit(self):
        with self.assertRaises(ValueError):
            convert_volume(1, "invalid_unit", "liter")

    def test_invalid_target_unit(self):
        with self.assertRaises(ValueError):
            convert_volume(1, "liter", "invalid_unit")

    def test_negative_volume(self):
        result = convert_volume(-10, "liter", "gallon")
        self.assertAlmostEqual(result, -10 / 3.78541, places=5)

if __name__ == "__main__":
    result_liters_to_gallons = convert_volume(1, "liter", "gallon")
    result_gallons_to_liters = convert_volume(1, "gallon", "liter")
    result_ml_to_liters = convert_volume(1000, "ml", "liter")
    result_zero = convert_volume(0, "gallon", "liter")
    result_large = convert_volume(1000000, "liter", "gallon")

    print(result_liters_to_gallons)
    print(result_gallons_to_liters)
    print(result_ml_to_liters)
    print(result_zero)
    print(result_large)

    unittest.main(exit=False)