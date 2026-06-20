import unittest

class DistanceConverter:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def to_meters(self):
        if self.unit == "m":
            return self.value
        elif self.unit == "km":
            return self.value * 1000
        elif self.unit == "cm":
            return self.value / 100
        elif self.unit == "mm":
            return self.value / 1000
        elif self.unit == "in":
            return self.value * 0.0254
        elif self.unit == "ft":
            return self.value * 0.3048
        elif self.unit == "yd":
            return self.value * 0.9144
        elif self.unit == "mi":
            return self.value * 1609.34
        else:
            raise ValueError(f"Unsupported unit: {self.unit}")

    def to_unit(self, target_unit):
        meters = self.to_meters()
        if target_unit == "m":
            return meters
        elif target_unit == "km":
            return meters / 1000
        elif target_unit == "cm":
            return meters * 100
        elif target_unit == "mm":
            return meters * 1000
        elif target_unit == "in":
            return meters / 0.0254
        elif target_unit == "ft":
            return meters / 0.3048
        elif target_unit == "yd":
            return meters / 0.9144
        elif target_unit == "mi":
            return meters / 1609.34
        else:
            raise ValueError(f"Unsupported target unit: {target_unit}")

class TestDistanceConverter(unittest.TestCase):

    def test_kilometers_to_meters(self):
        converter = DistanceConverter(2, "km")
        self.assertEqual(converter.to_meters(), 2000)

    def test_meters_to_kilometers(self):
        converter = DistanceConverter(5000, "m")
        self.assertEqual(converter.to_unit("km"), 5)

    def test_miles_to_meters(self):
        converter = DistanceConverter(1, "mi")
        self.assertAlmostEqual(converter.to_meters(), 1609.34, places=2)

    def test_meters_to_miles(self):
        converter = DistanceConverter(1609.34, "m")
        self.assertAlmostEqual(converter.to_unit("mi"), 1, places=2)

    def test_feet_to_meters(self):
        converter = DistanceConverter(10, "ft")
        self.assertAlmostEqual(converter.to_meters(), 3.048, places=3)

    def test_meters_to_feet(self):
        converter = DistanceConverter(3.048, "m")
        self.assertAlmostEqual(converter.to_unit("ft"), 10, places=2)

    def test_inches_to_meters(self):
        converter = DistanceConverter(100, "in")
        self.assertAlmostEqual(converter.to_meters(), 2.54, places=2)

    def test_meters_to_inches(self):
        converter = DistanceConverter(2.54, "m")
        self.assertAlmostEqual(converter.to_unit("in"), 100, places=2)

    def test_centimeters_to_meters(self):
        converter = DistanceConverter(250, "cm")
        self.assertEqual(converter.to_meters(), 2.5)

    def test_meters_to_centimeters(self):
        converter = DistanceConverter(2.5, "m")
        self.assertEqual(converter.to_unit("cm"), 250)

    def test_yards_to_meters(self):
        converter = DistanceConverter(5, "yd")
        self.assertAlmostEqual(converter.to_meters(), 4.572, places=3)

    def test_meters_to_yards(self):
        converter = DistanceConverter(4.572, "m")
        self.assertAlmostEqual(converter.to_unit("yd"), 5, places=2)

    def test_millimeters_to_meters(self):
        converter = DistanceConverter(1500, "mm")
        self.assertEqual(converter.to_meters(), 1.5)

    def test_meters_to_millimeters(self):
        converter = DistanceConverter(1.5, "m")
        self.assertEqual(converter.to_unit("mm"), 1500)

    def test_invalid_source_unit(self):
        converter = DistanceConverter(10, "xyz")
        with self.assertRaises(ValueError):
            converter.to_meters()

    def test_invalid_target_unit(self):
        converter = DistanceConverter(10, "m")
        with self.assertRaises(ValueError):
            converter.to_unit("xyz")

if __name__ == '__main__':
    converter = DistanceConverter(10, "km")
    print(converter.to_meters())
    print(converter.to_unit("mi"))
    print(converter.to_unit("ft"))
    print(converter.to_unit("cm"))