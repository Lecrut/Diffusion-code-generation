import unittest

class DistanceConverter:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def to_meters(self):
        if self.unit == "m":
            return self.value
        if self.unit == "km":
            return self.value * 1000.0
        if self.unit == "cm":
            return self.value / 100.0
        if self.unit == "mm":
            return self.value / 1000.0
        if self.unit == "mi":
            return self.value * 1609.34
        if self.unit == "yd":
            return self.value * 0.9144
        if self.unit == "ft":
            return self.value * 0.3048
        if self.unit == "in":
            return self.value * 0.0254
        raise ValueError(f"Unknown unit: {self.unit}")

    def to_kilometers(self):
        return self.to_meters() / 1000.0

    def to_centimeters(self):
        return self.to_meters() * 100.0

    def to_millimeters(self):
        return self.to_meters() * 1000.0

    def to_miles(self):
        return self.to_meters() / 1609.34

    def to_yards(self):
        return self.to_meters() / 0.9144

    def to_feet(self):
        return self.to_meters() / 0.3048

    def to_inches(self):
        return self.to_meters() / 0.0254

    def convert(self, target_unit):
        target_methods = {
            "m": self.to_meters,
            "km": self.to_kilometers,
            "cm": self.to_centimeters,
            "mm": self.to_millimeters,
            "mi": self.to_miles,
            "yd": self.to_yards,
            "ft": self.to_feet,
            "in": self.to_inches
        }
        if target_unit not in target_methods:
            raise ValueError(f"Unknown target unit: {target_unit}")
        return target_methods[target_unit]()

class TestDistanceConverter(unittest.TestCase):
    def test_meters_to_meters(self):
        converter = DistanceConverter(50, "m")
        self.assertAlmostEqual(converter.to_meters(), 50.0)

    def test_kilometers_to_meters(self):
        converter = DistanceConverter(2.5, "km")
        self.assertAlmostEqual(converter.to_meters(), 2500.0)

    def test_centimeters_to_meters(self):
        converter = DistanceConverter(150, "cm")
        self.assertAlmostEqual(converter.to_meters(), 1.5)

    def test_millimeters_to_meters(self):
        converter = DistanceConverter(500, "mm")
        self.assertAlmostEqual(converter.to_meters(), 0.5)

    def test_miles_to_meters(self):
        converter = DistanceConverter(1, "mi")
        self.assertAlmostEqual(converter.to_meters(), 1609.34)

    def test_yards_to_meters(self):
        converter = DistanceConverter(2, "yd")
        self.assertAlmostEqual(converter.to_meters(), 1.8288)

    def test_feet_to_meters(self):
        converter = DistanceConverter(10, "ft")
        self.assertAlmostEqual(converter.to_meters(), 3.048)

    def test_inches_to_meters(self):
        converter = DistanceConverter(12, "in")
        self.assertAlmostEqual(converter.to_meters(), 0.3048)

    def test_unknown_unit_initialization(self):
        with self.assertRaises(ValueError):
            DistanceConverter(10, "xyz")

    def test_conversion_chain_km_to_cm(self):
        converter = DistanceConverter(1, "km")
        self.assertAlmostEqual(converter.to_centimeters(), 100000.0)

    def test_conversion_chain_miles_to_feet(self):
        converter = DistanceConverter(1, "mi")
        self.assertAlmostEqual(converter.to_feet(), 5279.999999999999)

    def test_convert_method_specific_target(self):
        converter = DistanceConverter(100, "cm")
        result = converter.convert("m")
        self.assertAlmostEqual(result, 1.0)

    def test_convert_method_unknown_target(self):
        converter = DistanceConverter(10, "m")
        with self.assertRaises(ValueError):
            converter.convert("unknown")

    def test_meters_to_kilometers(self):
        converter = DistanceConverter(5000, "m")
        self.assertAlmostEqual(converter.to_kilometers(), 5.0)

    def test_meters_to_miles(self):
        converter = DistanceConverter(1609.34, "m")
        self.assertAlmostEqual(converter.to_miles(), 1.0)

if __name__ == '__main__':
    converter = DistanceConverter(1.5, "km")
    print(converter.to_meters())
    print(converter.convert("cm"))
    print(converter.to_feet())
    unittest.main()