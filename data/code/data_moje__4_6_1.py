import unittest
from math import isclose

class DistanceConverter:
    def __init__(self, value, from_unit='meters'):
        self.value = value
        self.from_unit = from_unit.lower()
        self.conversions = {
            'meters': 1.0,
            'kilometers': 1000.0,
            'centimeters': 0.01,
            'millimeters': 0.001,
            'miles': 1609.344,
            'yards': 0.9144,
            'feet': 0.3048,
            'inches': 0.0254
        }

    def _to_meters(self):
        if self.from_unit not in self.conversions:
            raise ValueError(f"Unsupported source unit: {self.from_unit}")
        return self.value * self.conversions[self.from_unit]

    def convert(self, to_unit):
        to_unit = to_unit.lower()
        if to_unit not in self.conversions:
            raise ValueError(f"Unsupported target unit: {to_unit}")
        meters = self._to_meters()
        return meters / self.conversions[to_unit]

class TestDistanceConverter(unittest.TestCase):
    def test_meters_to_meters(self):
        converter = DistanceConverter(10, 'meters')
        self.assertAlmostEqual(converter.convert('meters'), 10.0, places=5)

    def test_meters_to_kilometers(self):
        converter = DistanceConverter(1000, 'meters')
        self.assertAlmostEqual(converter.convert('kilometers'), 1.0, places=5)

    def test_meters_to_centimeters(self):
        converter = DistanceConverter(1, 'meters')
        self.assertAlmostEqual(converter.convert('centimeters'), 100.0, places=5)

    def test_meters_to_millimeters(self):
        converter = DistanceConverter(1, 'meters')
        self.assertAlmostEqual(converter.convert('millimeters'), 1000.0, places=5)

    def test_meters_to_miles(self):
        converter = DistanceConverter(1609.344, 'meters')
        self.assertAlmostEqual(converter.convert('miles'), 1.0, places=5)

    def test_meters_to_yards(self):
        converter = DistanceConverter(0.9144, 'meters')
        self.assertAlmostEqual(converter.convert('yards'), 1.0, places=5)

    def test_meters_to_feet(self):
        converter = DistanceConverter(0.3048, 'meters')
        self.assertAlmostEqual(converter.convert('feet'), 1.0, places=5)

    def test_meters_to_inches(self):
        converter = DistanceConverter(0.0254, 'meters')
        self.assertAlmostEqual(converter.convert('inches'), 1.0, places=5)

    def test_kilometers_to_meters(self):
        converter = DistanceConverter(1, 'kilometers')
        self.assertAlmostEqual(converter.convert('meters'), 1000.0, places=5)

    def test_kilometers_to_miles(self):
        converter = DistanceConverter(1.609344, 'kilometers')
        self.assertAlmostEqual(converter.convert('miles'), 1.0, places=5)

    def test_miles_to_kilometers(self):
        converter = DistanceConverter(1, 'miles')
        self.assertAlmostEqual(converter.convert('kilometers'), 1.609344, places=5)

    def test_feet_to_meters(self):
        converter = DistanceConverter(1, 'feet')
        self.assertAlmostEqual(converter.convert('meters'), 0.3048, places=5)

    def test_inches_to_centimeters(self):
        converter = DistanceConverter(1, 'inches')
        self.assertAlmostEqual(converter.convert('centimeters'), 2.54, places=5)

    def test_yards_to_feet(self):
        converter = DistanceConverter(1, 'yards')
        self.assertAlmostEqual(converter.convert('feet'), 3.0, places=5)

    def test_case_insensitivity(self):
        converter = DistanceConverter(10, 'Meters')
        self.assertAlmostEqual(converter.convert('Kilometers'), 0.01, places=5)

    def test_invalid_from_unit(self):
        with self.assertRaises(ValueError):
            DistanceConverter(1, 'parsecs').convert('meters')

    def test_invalid_to_unit(self):
        converter = DistanceConverter(1, 'meters')
        with self.assertRaises(ValueError):
            converter.convert('parsecs')

    def test_zero_distance(self):
        converter = DistanceConverter(0, 'meters')
        self.assertAlmostEqual(converter.convert('kilometers'), 0.0, places=5)

    def test_negative_distance(self):
        converter = DistanceConverter(-10, 'meters')
        self.assertAlmostEqual(converter.convert('kilometers'), -0.01, places=5)

    def test_large_distance(self):
        converter = DistanceConverter(1e6, 'meters')
        self.assertAlmostEqual(converter.convert('kilometers'), 1000.0, places=5)

if __name__ == '__main__':
    converter = DistanceConverter(5, 'kilometers')
    result = converter.convert('miles')
    print(result)

    converter2 = DistanceConverter(100, 'feet')
    result2 = converter2.convert('meters')
    print(result2)

    unittest.main()