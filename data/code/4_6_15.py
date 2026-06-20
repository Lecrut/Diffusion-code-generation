import unittest
from decimal import Decimal

class DistanceConverter:
    def __init__(self):
        self.meters = 0

    def set_meters(self, value):
        self.meters = float(value)

    def get_meters(self):
        return self.meters

    def get_kilometers(self):
        return self.meters / 1000

    def get_miles(self):
        return self.meters * 0.000621371

    def get_feet(self):
        return self.meters * 3.28084

    def get_inches(self):
        return self.meters * 39.3701

class TestDistanceConverter(unittest.TestCase):
    def test_init_zero(self):
        converter = DistanceConverter()
        self.assertEqual(converter.get_meters(), 0)

    def test_set_meters(self):
        converter = DistanceConverter()
        converter.set_meters(100)
        self.assertEqual(converter.get_meters(), 100.0)

    def test_set_meters_zero(self):
        converter = DistanceConverter()
        converter.set_meters(0)
        self.assertEqual(converter.get_meters(), 0.0)

    def test_set_meters_negative(self):
        converter = DistanceConverter()
        converter.set_meters(-50)
        self.assertEqual(converter.get_meters(), -50.0)

    def test_get_kilometers_positive(self):
        converter = DistanceConverter()
        converter.set_meters(1000)
        self.assertAlmostEqual(converter.get_kilometers(), 1.0, places=5)

    def test_get_kilometers_zero(self):
        converter = DistanceConverter()
        converter.set_meters(0)
        self.assertEqual(converter.get_kilometers(), 0.0)

    def test_get_kilometers_negative(self):
        converter = DistanceConverter()
        converter.set_meters(-1000)
        self.assertAlmostEqual(converter.get_kilometers(), -1.0, places=5)

    def test_get_miles_positive(self):
        converter = DistanceConverter()
        converter.set_meters(1609.34)
        self.assertAlmostEqual(converter.get_miles(), 1.0, places=4)

    def test_get_miles_zero(self):
        converter = DistanceConverter()
        converter.set_meters(0)
        self.assertEqual(converter.get_miles(), 0.0)

    def test_get_feet_positive(self):
        converter = DistanceConverter()
        converter.set_meters(1)
        self.assertAlmostEqual(converter.get_feet(), 3.28084, places=5)

    def test_get_feet_zero(self):
        converter = DistanceConverter()
        converter.set_meters(0)
        self.assertEqual(converter.get_feet(), 0.0)

    def test_get_inches_positive(self):
        converter = DistanceConverter()
        converter.set_meters(1)
        self.assertAlmostEqual(converter.get_inches(), 39.3701, places=4)

    def test_get_inches_zero(self):
        converter = DistanceConverter()
        converter.set_meters(0)
        self.assertEqual(converter.get_inches(), 0.0)

    def test_conversion_chain_meters_to_km_and_back(self):
        converter = DistanceConverter()
        initial_meters = 5000
        converter.set_meters(initial_meters)
        km = converter.get_kilometers()
        result_meters = km * 1000
        self.assertAlmostEqual(result_meters, initial_meters, places=5)

    def test_conversion_chain_meters_to_miles_and_back(self):
        converter = DistanceConverter()
        initial_meters = 8000
        converter.set_meters(initial_meters)
        miles = converter.get_miles()
        result_meters = miles / 0.000621371
        self.assertAlmostEqual(result_meters, initial_meters, places=4)

    def test_large_value(self):
        converter = DistanceConverter()
        converter.set_meters(1000000)
        self.assertEqual(converter.get_kilometers(), 1000.0)
        self.assertAlmostEqual(converter.get_miles(), 621.371, places=3)

    def test_small_value(self):
        converter = DistanceConverter()
        converter.set_meters(0.001)
        self.assertEqual(converter.get_meters(), 0.001)
        self.assertAlmostEqual(converter.get_kilometers(), 1e-6, places=9)

if __name__ == '__main__':
    converter = DistanceConverter()
    converter.set_meters(1000)
    km_value = converter.get_kilometers()
    miles_value = converter.get_miles()
    feet_value = converter.get_feet()
    inches_value = converter.get_inches()
    print(km_value)
    print(miles_value)
    print(feet_value)
    print(inches_value)