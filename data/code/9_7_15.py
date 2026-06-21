import unittest

class VolumeConverter:
    CONVERSION_FACTORS = {
        ("liters", "milliliters"): 1000.0,
        ("milliliters", "liters"): 0.001,
        ("liters", "gallons"): 0.264172,
        ("gallons", "liters"): 3.78541,
        ("liters", "cubic_meters"): 0.001,
        ("cubic_meters", "liters"): 1000.0,
        ("gallons", "milliliters"): 3785.41,
        ("milliliters", "gallons"): 0.000264172,
        ("cubic_meters", "gallons"): 264.172,
        ("gallons", "cubic_meters"): 0.00378541,
        ("cubic_meters", "milliliters"): 1000000.0,
        ("milliliters", "cubic_meters"): 0.000001,
    }

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if value < 0:
            raise ValueError("Volume cannot be negative")
        if from_unit not in self.CONVERSION_FACTORS or to_unit not in self.CONVERSION_FACTORS:
            supported = set()
            for key in self.CONVERSION_FACTORS:
                supported.update(key)
            if from_unit not in supported:
                raise ValueError(f"Unsupported from_unit: {from_unit}")
            if to_unit not in supported:
                raise ValueError(f"Unsupported to_unit: {to_unit}")
        key = (from_unit, to_unit)
        if key in self.CONVERSION_FACTORS:
            factor = self.CONVERSION_FACTORS[key]
            return value * factor
        raise ValueError(f"No direct conversion path from {from_unit} to {to_unit}")

class TestVolumeConverter(unittest.TestCase):
    def setUp(self):
        self.converter = VolumeConverter()

    def test_identity_conversion(self):
        self.assertAlmostEqual(self.converter.convert(5.0, "liters", "liters"), 5.0)

    def test_liters_to_milliliters(self):
        self.assertAlmostEqual(self.converter.convert(1.0, "liters", "milliliters"), 1000.0)

    def test_milliliters_to_liters(self):
        self.assertAlmostEqual(self.converter.convert(500.0, "milliliters", "liters"), 0.5)

    def test_liters_to_gallons(self):
        self.assertAlmostEqual(
            self.converter.convert(1.0, "liters", "gallons"), 0.264172, places=5
        )

    def test_gallons_to_liters(self):
        self.assertAlmostEqual(
            self.converter.convert(1.0, "gallons", "liters"), 3.78541, places=5
        )

    def test_zero_volume(self):
        self.assertAlmostEqual(self.converter.convert(0.0, "liters", "gallons"), 0.0)

    def test_large_number(self):
        large_value = 1e9
        result = self.converter.convert(large_value, "liters", "milliliters")
        self.assertAlmostEqual(result, large_value * 1000.0)

    def test_negative_volume_raises_error(self):
        with self.assertRaises(ValueError):
            self.converter.convert(-5.0, "liters", "milliliters")

    def test_unsupported_from_unit(self):
        with self.assertRaises(ValueError):
            self.converter.convert(5.0, "ounces", "liters")

    def test_unsupported_to_unit(self):
        with self.assertRaises(ValueError):
            self.converter.convert(5.0, "liters", "pints")

    def test_cubic_meters_to_liters(self):
        self.assertAlmostEqual(
            self.converter.convert(1.0, "cubic_meters", "liters"), 1000.0
        )

    def test_gallons_to_cubic_meters(self):
        self.assertAlmostEqual(
            self.converter.convert(1.0, "gallons", "cubic_meters"), 0.00378541, places=6
        )

    def test_small_positive_number(self):
        small_value = 1e-9
        result = self.converter.convert(small_value, "gallons", "milliliters")
        expected = small_value * 3785.41
        self.assertAlmostEqual(result, expected, places=15)

    def test_round_trip_conversion(self):
        original = 123.456
        converted_to_ml = self.converter.convert(original, "liters", "milliliters")
        converted_back = self.converter.convert(converted_to_ml, "milliliters", "liters")
        self.assertAlmostEqual(converted_back, original, places=5)

    def test_multiple_unit_conversions(self):
        liters_to_gallons = self.converter.convert(10.0, "liters", "gallons")
        gallons_to_liters = self.converter.convert(liters_to_gallons, "gallons", "liters")
        self.assertAlmostEqual(gallons_to_liters, 10.0, places=5)

if __name__ == "__main__":
    converter = VolumeConverter()
    print(converter.convert(1.0, "liters", "milliliters"))
    print(converter.convert(0.0, "gallons", "liters"))
    print(converter.convert(1e6, "liters", "cubic_meters"))
    print(converter.convert(5.5, "gallons", "milliliters"))
    unittest.main(argv=[''], exit=False, verbosity=2)