import unittest
import math

class DistanceConverter:
    def __init__(self, distance_in_meters):
        self.distance_in_meters = distance_in_meters

    def to_kilometers(self):
        return self.distance_in_meters / 1000.0

    def to_miles(self):
        return self.distance_in_meters / 1609.344

    def to_feet(self):
        return self.distance_in_meters * 3.28084

    def to_centimeters(self):
        return self.distance_in_meters * 100.0

    def to_millimeters(self):
        return self.distance_in_meters * 1000.0

    def to_inches(self):
        return self.distance_in_meters * 39.3701

    def get_meters(self):
        return self.distance_in_meters

class TestDistanceConverter(unittest.TestCase):
    def test_to_kilometers(self):
        converter = DistanceConverter(1000.0)
        self.assertAlmostEqual(converter.to_kilometers(), 1.0, places=5)

    def test_to_kilometers_zero(self):
        converter = DistanceConverter(0.0)
        self.assertAlmostEqual(converter.to_kilometers(), 0.0, places=5)

    def test_to_miles(self):
        converter = DistanceConverter(1609.344)
        self.assertAlmostEqual(converter.to_miles(), 1.0, places=5)

    def test_to_miles_zero(self):
        converter = DistanceConverter(0.0)
        self.assertAlmostEqual(converter.to_miles(), 0.0, places=5)

    def test_to_feet(self):
        converter = DistanceConverter(1.0)
        self.assertAlmostEqual(converter.to_feet(), 3.28084, places=5)

    def test_to_feet_zero(self):
        converter = DistanceConverter(0.0)
        self.assertAlmostEqual(converter.to_feet(), 0.0, places=5)

    def test_to_centimeters(self):
        converter = DistanceConverter(1.0)
        self.assertAlmostEqual(converter.to_centimeters(), 100.0, places=5)

    def test_to_centimeters_zero(self):
        converter = DistanceConverter(0.0)
        self.assertAlmostEqual(converter.to_centimeters(), 0.0, places=5)

    def test_to_millimeters(self):
        converter = DistanceConverter(1.0)
        self.assertAlmostEqual(converter.to_millimeters(), 1000.0, places=5)

    def test_to_millimeters_zero(self):
        converter = DistanceConverter(0.0)
        self.assertAlmostEqual(converter.to_millimeters(), 0.0, places=5)

    def test_to_inches(self):
        converter = DistanceConverter(1.0)
        self.assertAlmostEqual(converter.to_inches(), 39.3701, places=5)

    def test_to_inches_zero(self):
        converter = DistanceConverter(0.0)
        self.assertAlmostEqual(converter.to_inches(), 0.0, places=5)

    def test_get_meters(self):
        converter = DistanceConverter(500.5)
        self.assertAlmostEqual(converter.get_meters(), 500.5, places=5)

    def test_negative_distance(self):
        converter = DistanceConverter(-10.0)
        self.assertAlmostEqual(converter.to_kilometers(), -0.01, places=5)
        self.assertAlmostEqual(converter.to_miles(), -0.0062137, places=7)

    def test_large_distance(self):
        converter = DistanceConverter(1000000.0)
        self.assertAlmostEqual(converter.to_kilometers(), 1000.0, places=5)
        self.assertAlmostEqual(converter.to_miles(), 621.371, places=3)

if __name__ == '__main__':
    converter = DistanceConverter(5000.0)
    print(converter.to_kilometers())
    print(converter.to_miles())
    print(converter.to_feet())
    print(converter.to_centimeters())
    print(converter.to_millimeters())
    print(converter.to_inches())
    print(converter.get_meters())
    unittest.main()