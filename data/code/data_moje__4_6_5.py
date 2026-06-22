import unittest
import math

class DistanceConverter:
    METERS_PER_KM = 1000
    METERS_PER_MILE = 1609.34
    METERS_PER_METER = 1
    METERS_PER_YARD = 0.9144
    METERS_PER_INCH = 0.0254

    def __init__(self, value, unit):
        if value < 0:
            raise ValueError("Distance cannot be negative")
        valid_units = ["km", "m", "mi", "yd", "in"]
        if unit not in valid_units:
            raise ValueError(f"Invalid unit: {unit}. Must be one of {valid_units}")
        self.value = float(value)
        self.unit = unit.lower()
        self.meters = self._to_meters(self.value, self.unit)

    def _to_meters(self, val, u):
        if u == "km":
            return val * self.METERS_PER_KM
        elif u == "mi":
            return val * self.METERS_PER_MILE
        elif u == "yd":
            return val * self.METERS_PER_YARD
        elif u == "in":
            return val * self.METERS_PER_INCH
        else:
            return val * self.METERS_PER_METER

    def convert(self, target_unit):
        valid_units = ["km", "m", "mi", "yd", "in"]
        if target_unit not in valid_units:
            raise ValueError(f"Invalid target unit: {target_unit}. Must be one of {valid_units}")
        target_unit = target_unit.lower()
        if target_unit == "m":
            return self.meters
        elif target_unit == "km":
            return self.meters / self.METERS_PER_KM
        elif target_unit == "mi":
            return self.meters / self.METERS_PER_MILE
        elif target_unit == "yd":
            return self.meters / self.METERS_PER_YARD
        elif target_unit == "in":
            return self.meters / self.METERS_PER_INCH
        return 0.0

class TestDistanceConverter(unittest.TestCase):
    def test_km_to_m(self):
        converter = DistanceConverter(1, "km")
        self.assertAlmostEqual(converter.convert("m"), 1000.0, places=5)

    def test_m_to_km(self):
        converter = DistanceConverter(1000, "m")
        self.assertAlmostEqual(converter.convert("km"), 1.0, places=5)

    def test_mi_to_m(self):
        converter = DistanceConverter(1, "mi")
        self.assertAlmostEqual(converter.convert("m"), 1609.34, places=5)

    def test_m_to_mi(self):
        converter = DistanceConverter(1609.34, "m")
        self.assertAlmostEqual(converter.convert("mi"), 1.0, places=5)

    def test_yd_to_m(self):
        converter = DistanceConverter(1, "yd")
        self.assertAlmostEqual(converter.convert("m"), 0.9144, places=5)

    def test_m_to_yd(self):
        converter = DistanceConverter(0.9144, "m")
        self.assertAlmostEqual(converter.convert("yd"), 1.0, places=5)

    def test_in_to_m(self):
        converter = DistanceConverter(1, "in")
        self.assertAlmostEqual(converter.convert("m"), 0.0254, places=5)

    def test_m_to_in(self):
        converter = DistanceConverter(0.0254, "m")
        self.assertAlmostEqual(converter.convert("in"), 1.0, places=5)

    def test_km_to_mi(self):
        converter = DistanceConverter(1.60934, "km")
        self.assertAlmostEqual(converter.convert("mi"), 1.0, places=5)

    def test_mi_to_yd(self):
        converter = DistanceConverter(1, "mi")
        expected = 1760.0
        self.assertAlmostEqual(converter.convert("yd"), expected, places=5)

    def test_invalid_unit_input(self):
        with self.assertRaises(ValueError):
            DistanceConverter(1, "ft")

    def test_invalid_target_unit(self):
        converter = DistanceConverter(1, "m")
        with self.assertRaises(ValueError):
            converter.convert("ft")

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            DistanceConverter(-5, "m")

    def test_same_unit(self):
        converter = DistanceConverter(42, "m")
        self.assertAlmostEqual(converter.convert("m"), 42.0, places=5)

if __name__ == '__main__':
    converter = DistanceConverter(1, "km")
    print(converter.convert("mi"))
    print(converter.convert("m"))
    print(converter.convert("in"))
    converter2 = DistanceConverter(5280, "ft".replace("ft", "m"))
    print(converter2.convert("km"))
    unittest.main(exit=False)