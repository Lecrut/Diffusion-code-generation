import unittest

class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            "l": 1.0,
            "ml": 0.001,
            "gal": 3.78541,
            "qt": 0.946353,
            "pt": 0.473176,
            "cup": 0.236588,
            "floz": 0.0295735,
            "tbsp": 0.0147868,
            "tsp": 0.00492892,
            "m3": 1000.0,
            "cm3": 0.001,
        }

    def convert(self, volume, from_unit, to_unit):
        if volume < 0:
            raise ValueError("Volume cannot be negative")
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Unknown source unit: {from_unit}")
        if to_unit not in self.conversion_factors:
            raise ValueError(f"Unknown target unit: {to_unit}")
        base_volume = volume * self.conversion_factors[from_unit]
        return base_volume / self.conversion_factors[to_unit]

def convert_volume(volume, from_unit, to_unit):
    converter = VolumeConverter()
    return converter.convert(volume, from_unit, to_unit)

class TestVolumeConversion(unittest.TestCase):
    def test_zero_volume(self):
        self.assertAlmostEqual(convert_volume(0, "l", "ml"), 0.0)

    def test_large_volume_liters_to_ml(self):
        self.assertAlmostEqual(convert_volume(1000000, "l", "ml"), 1000000000.0)

    def test_gallons_to_liters(self):
        self.assertAlmostEqual(convert_volume(1, "gal", "l"), 3.78541, places=5)

    def test_milliliters_to_liters(self):
        self.assertAlmostEqual(convert_volume(1000, "ml", "l"), 1.0)

    def test_negative_volume_raises_error(self):
        with self.assertRaises(ValueError):
            convert_volume(-1, "l", "ml")

    def test_unknown_source_unit_raises_error(self):
        with self.assertRaises(ValueError):
            convert_volume(1, "invalid", "ml")

    def test_unknown_target_unit_raises_error(self):
        with self.assertRaises(ValueError):
            convert_volume(1, "l", "invalid")

    def test_cubic_meters_to_liters(self):
        self.assertAlmostEqual(convert_volume(1, "m3", "l"), 1000.0)

    def test_cups_to_tablespoons(self):
        cups_to_tbsp = convert_volume(1, "cup", "tbsp")
        expected = 0.236588 / 0.0147868
        self.assertAlmostEqual(cups_to_tbsp, expected, places=4)

    def test_floz_to_tsp(self):
        floz_to_tsp = convert_volume(1, "floz", "tsp")
        expected = 0.0295735 / 0.00492892
        self.assertAlmostEqual(floz_to_tsp, expected, places=4)

if __name__ == "__main__":
    result = convert_volume(1, "l", "ml")
    print(result)
    result2 = convert_volume(1, "gal", "l")
    print(result2)
    unittest.main()